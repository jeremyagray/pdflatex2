# ******************************************************************************
#
# pdflatex2, a Python/PDFLaTeX interface.
#
# Copyright 2022 Jeremy A Gray <gray@flyquackswim.com>.  All rights
# reserved.
# Copyright 2019 Marcelo Bello.
#
# SPDX-License-Identifier: MIT
#
# ******************************************************************************

"""pdflatex tests."""

import datetime

import pytest

from pdflatex2 import PDFLaTeX


def test_pdflatex_from_binary_string_job():
    """Should set the job correctly."""
    pdf = PDFLaTeX.from_binary_string(b"", "bob")

    assert pdf.job == "bob"

    pdf = PDFLaTeX.from_binary_string(b"")

    assert pytest.approx(int(pdf.job)) == int(
        datetime.datetime.utcnow().timestamp() * 1000
    )
