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

"""pdflatex tests."""

import uuid

import pytest

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


def test_pdflatex_sets_default_runs():
    """Should set the default number of runs."""
    pdf = PDFLaTeX("")

    assert pdf.runs == 1


def test_pdflatex_refuses_to_exceed_max_runs():
    """Should not exceed the maximum number of runs."""
    pdf = PDFLaTeX("", runs=7)

    assert pdf.runs == 5


def test_pdflatex_warns_on_excessive_runs():
    """Should warn on excessive runs."""
    with pytest.warns(UserWarning, match="maximum allowed pdflatex runs is 5"):
        PDFLaTeX("", runs=7)


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

    assert int(doc.return_status) == 0


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
