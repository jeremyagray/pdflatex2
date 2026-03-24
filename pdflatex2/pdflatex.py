# ******************************************************************************
#
# pdflatex2, a Python/PDFLaTeX interface.
#
# Copyright 2022-2026 Jeremy A Gray <gray@flyquackswim.com>.  All
# rights reserved.
#
# Copyright 2019 Marcelo Bello.
#
# SPDX-License-Identifier: MIT
#
# ******************************************************************************

"""PDFLaTeX class and utilities."""

import subprocess  # nosec B404
import tempfile
import uuid
import warnings
from pathlib import Path

_max_runs = 5

_INTERACTION_MODES = (
    "batchmode",
    "nonstopmode",
    "scrollmode",
    "errorstopmode",
)

_CONTROLLED_PDFLATEX_OPTIONS = (  # dead: disable
    "interaction",
    "job-name",
    "output-directory",
)

_INTERACTIVE_PDFLATEX_OPTIONS = (  # dead: disable
    "help",
    "version",
)

_PDFLATEX_INT_OPTIONS = (  # dead: disable
    "buf-size",
    "error-line",
    "extra-mem-bot",
    "extra-mem-top",
    "font-max",
    "font-mem-size",
    "half-error-line",
    "hash-extra",
    "include-directory",
    "main-memory",
    "max-in-open",
    "max-print-line",
    "max-strings",
    "nest-size",
    "param-size",
    "pool-free",
    "pool-size",
    "save-size",
    "stack-size",
    "string-vacancies",
    "synctex",
    "trie-size",
)

_PDFLATEX_STRING_OPTIONS = (  # dead: disable
    "alias",
    "aux-directory",
    "job-time",
    "output-format",
    "record-package-usages",
    "tcx",
    "trace",
    "undump",
)

_PDFLATEX_BINARY_OPTIONS = (  # dead: disable
    "c-style-errors",
    "disable-8bit-chars",
    "disable-installer",
    "disable-write18",
    "dont-parse-first-line",
    "draftmode",
    "enable-8bit-chars",
    "enable-enctex",
    "enable-etex",
    "enable-installer",
    "enable-mltex",
    "enable-write18",
    "halt-on-error",
    "initialize",
    "no-c-style-errors",
    "parse-first-line",
    "quiet",
    "recorder",
    "restrict-write18",
    "src-specials",
    "time-statistics",
    "verbose",
)


class PDFLaTeX:
    """PDFLaTeX interaction."""

    def __init__(self, latex, mode="batchmode", runs=1):
        """Initialize a ``pdflatex`` interaction.

        Parameters
        ----------
        latex : str
            A string containing TeX or LaTeX source with which to
            generate the PDF.
        mode : str
            Set the mode for pdflatex.
        runs : int
            Number of pdflatex runs to attempt.

        """
        self.latex = latex
        self.interaction = mode
        self.runs = runs
        self.job = uuid.uuid4()
        self.pdf = None
        self.aux = None
        self.log = None

    @property
    def interaction(self):
        """Get the interaction mode."""
        return self._interaction

    @interaction.setter
    def interaction(self, mode):
        """Set the interaction mode."""
        if mode in _INTERACTION_MODES:
            self._interaction = mode
        else:
            raise ValueError(
                f"invalid interaction mode '{mode}'; "
                f"choose from valid modes:  '{', '.join(_INTERACTION_MODES)}'"
            )

        return self._interaction

    @interaction.deleter
    def interaction(self):
        """Delete the interaction mode."""
        raise AttributeError(
            "interaction mode required; set to ``batchmode`` for default behavior"
        )

    @property
    def runs(self):
        """Get the number of pdflatex runs."""
        return self._runs

    @runs.setter
    def runs(self, num):
        """Set the number of pdflatex runs."""
        if num > _max_runs:
            warnings.warn(
                f"maximum allowed pdflatex runs is {_max_runs}",
                stacklevel=2,
            )

        self._runs = min(num, _max_runs)

        return self._runs

    @classmethod
    def from_string(cls, latex, mode="batchmode", **kwargs):
        """Instantiate from a string.

        Instantiate from a string, like from a TeX/LaTeX file.

        Parameters
        ----------
        cls
            The ``PDFLaTeX`` class.
        latex : str
            A string containing TeX or LaTeX source with which to
            generate the PDF.
        mode : str
            Set the mode for pdflatex.
        kwargs : dict
            Options to be passed to the ``PDFLaTeX`` class.

        """
        return cls(latex, mode, **kwargs)

    @classmethod
    def from_tex_file(cls, fn, mode="batchmode", **kwargs):  # dead: disable
        """Instantiate from a TeX/LaTeX file.

        Parameters
        ----------
        cls
            The ``PDFLaTeX`` class.
        fn : str
            A TeX/LaTeX file.
        mode : str
            Set the mode for pdflatex.
        kwargs : dict
            Options to be passed to the ``PDFLaTeX`` class.

        """
        with open(fn, "r") as f:
            return cls.from_string(f.read(), mode, **kwargs)

    @classmethod
    def from_jinja_template(cls, template, mode="batchmode", **kwargs):  # dead: disable
        """Instantiate from a Jinja template.

        Parameters
        ----------
        cls
            The ``PDFLaTeX`` class.
        template
            A Jinja2 template instance.
        mode : str
            Set the mode for pdflatex.
        kwargs : dict
            Options to be passed to the ``PDFLaTeX`` class.

        """
        return cls.from_string(template.render(**kwargs), mode)

    def compile(self):  # dead: disable
        """Compile the PDF with pdflatex.

        Compile the PDF with pdflatex.  Create a temporary directory
        for the compilation process.  Place the LaTeX to be compiled
        in a temporary file within that directory, compile it
        (multiple times if necessary), and then retrieve the compiled
        PDF, log, and auxiliary files from the temporary directory.
        """
        # Create tempoary storage.
        with tempfile.TemporaryDirectory() as td:
            # Set paths.
            td = Path(td)
            texfile = td / f"{self.job}.tex"
            pdffile = td / f"{self.job}.pdf"
            logfile = td / f"{self.job}.log"
            auxfile = td / f"{self.job}.aux"

            # Process instance data into pdflatex command options.
            args = (
                "pdflatex",
                f"-interaction={self.interaction}",
                f"-output-directory={td!s}",
                f"-job-name={self.job}",
                str(texfile),
            )

            # Write temporary LaTeX file.
            with open(texfile, "w") as f:
                f.write(self.latex)

            for _ in range(self.runs):
                fp = subprocess.run(  # noqa: S603
                    args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=False,
                )

            # Add status information from the pdflatex run.
            self.return_status = int(fp.returncode)
            self.stdout = str(fp.stdout)
            self.stderr = str(fp.stderr)

            def _maybe_retrieve_file(attr, fn, mode="r"):
                """Retrieve file contents, if present."""
                # Retrieve file contents.
                try:
                    with open(fn, mode) as f:
                        setattr(self, attr, f.read())

                except FileNotFoundError:
                    pass

            _maybe_retrieve_file("pdf", pdffile, mode="rb")
            _maybe_retrieve_file("log", logfile)
            _maybe_retrieve_file("aux", auxfile)

        return self
