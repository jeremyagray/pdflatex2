# ******************************************************************************
#
# pdflatex2, a Python/PDFLaTeX interface.
#
# Copyright 2022-2024 Jeremy A Gray <gray@flyquackswim.com>.  All
# rights reserved.
#
# Copyright 2019 Marcelo Bello.
#
# SPDX-License-Identifier: MIT
#
# ******************************************************************************

"""pdflatex tests."""

import uuid

import pytest
from jinja2 import DictLoader
from jinja2 import Environment

from pdflatex2 import PDFLaTeX

latex_txt = r"""\documentclass[10pt]{letter}

\pagestyle{empty}

\begin{document}
This is a test.
\end{document}
"""

latex_bin = latex_txt.encode()


def test_pdflatex_sets_default_job():
    """Should set the job."""
    pdf = PDFLaTeX("")

    assert pdf.job == uuid.UUID(str(pdf.job))


def test_pdflatex_sets_default_interaction():
    """Should set the default interaction."""
    pdf = PDFLaTeX("")

    assert pdf.interaction == "batchmode"


def test_pdflatex_rejects_bad_interactions():
    """Should reject a bad interaction."""
    with pytest.raises(ValueError):
        PDFLaTeX("", mode="bad")


def test_pdflatex_cowardly_refuses_to_delete_interaction():
    """Should cowardly refuse to delete the interaction mode."""
    with pytest.raises(AttributeError):
        pdf = PDFLaTeX("")
        del pdf.interaction


def test_pdflatex_compile_use_all_interactions():
    """Should compile a PDF with any interaction mode."""
    # Default.
    doc = PDFLaTeX(latex_txt)
    doc.compile()

    assert int(doc.return_status) == 0

    for mode in ("batchmode", "nonstopmode", "scrollmode", "errorstopmode"):
        doc = PDFLaTeX(latex_txt, mode)
        doc.compile()

        assert int(doc.return_status) == 0


def test_pdflatex_compile_captures_stdout():
    """Should capture STDOUT when compiling a PDF."""
    # Default.
    doc = PDFLaTeX(latex_txt)
    doc.compile()

    assert "This is pdfTeX" in doc.stdout


def test_pdflatex_handles_missing_pdf_file():
    """Should not stop on a missing pdf file."""
    doc = PDFLaTeX("")
    doc.compile()

    assert doc.pdf is None


def test_pdflatex_handles_missing_aux_file():
    """Should not stop on a missing aux file."""
    doc = PDFLaTeX("")
    doc.compile()

    assert doc.aux is None


def test_pdflatex_instantiate_from_string():
    """Should instantiate from a LaTeX string."""
    # Default.
    doc = PDFLaTeX.from_string(latex_txt)
    doc.compile()

    assert int(doc.return_status) == int(0)


def test_pdflatex_instantiate_from_file(fs):
    """Should instantiate from a LaTeX file."""
    fn = "test.tex"
    fs.create_file(fn)
    with open(fn, "w") as f:
        f.write(latex_txt)

    doc = PDFLaTeX.from_tex_file("test.tex")

    # Compilation fails due to the fake file system; check initialized
    # object.
    assert "This is a test." in doc.latex


def test_pdflatex_instantiate_from_jinja():
    """Should instantiate from a rendered Jinja2 template."""
    j2 = Environment(
        loader=DictLoader(
            {
                "template.tex": r"""\documentclass[10pt]{letter}

\pagestyle{empty}

\begin{document}
The key's value is \VAR{ key }.
\end{document}
""",
            }
        ),
        block_start_string=r"\BLOCK{",
        block_end_string="}",
        variable_start_string=r"\VAR{",
        variable_end_string="}",
        comment_start_string=r"\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=True,
    )

    template = j2.get_template("template.tex")
    doc = PDFLaTeX.from_jinja_template(template, key="blarney")
    doc.compile()

    assert "blarney" in doc.latex
    assert int(doc.return_status) == int(0)
