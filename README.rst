.. *****************************************************************************
..
.. pdflatex2, a Python/PDFLaTeX interface.
..
.. Copyright 2022-2024 Jeremy A Gray <gray@flyquackswim.com>.  All
.. rights reserved.
..
.. Copyright 2019 Marcelo Bello.
..
.. SPDX-License-Identifier: MIT
..
.. *****************************************************************************

===========
 pdflatex2
===========

A Python/PDFLaTeX interface.

..
   .. image:: https://badge.fury.io/py/pdflatex2.svg
      :target: https://badge.fury.io/py/pdflatex2
      :alt: PyPI Version
   .. image:: https://readthedocs.org/projects/pdflatex2/badge/?version=latest
      :target: https://pdflatex2.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Description
===========

This module to executes ``pdflatex`` in an easy and clean way,
capturing the output of a ``pdflatex`` run for further processing by
the user without keeping the array of output files normally associated
with ``TeX`` and friends.

pdflatex2 is a port of the original `pdflatex
<https://pypi.org/pdflatex>`_, version 0.1.3, by Marcelo Bello.

Installation
============

Install pdflatex2 with::

  pip install pdflatex2

or add as a poetry dependency.

Usage
=====

See the source and `documentation
<https://pdflatex2.readthedocs.io/en/latest/>`_ for complete
information.

Instantiation
-------------

The PDFLaTeX class can be instantiated directly::

  >>> from pdflatex2 import PDFLaTeX
  >>> doc = PDFLaTeX(src)
  >>> doc.compile()

or through helpers::

  >>> doc = PDFLaTeX.from_string(src)
  >>> doc = PDFLaTeX.from_tex_file(filename)
  >>> doc = PDFLaTeX.from_jinja_template(template, **kwargs)

Examples
--------

Output files are created in a temporary directory and are available
after compilation on the ``PDFLaTeX`` object..

Create a PDF file from a string::

  >>> from pdflatex2 import PDFLaTeX
  >>> with open("file.tex", "r") as f:
  ...     pdf = PDFLaTeX.from_string(f.read())
  >>> pdf.compile()

The method ``compile()`` stores all information on the ``PDFLaTeX``
instance.

Create a PDF from a file::

  >>> from pdflatex2 import PDFLaTeX
  >>> pdf = PDFLaTeX.from_tex_file("file.tex")
  >>> pdf.compile()

Create PDF from a Jinja template::

  >>> import jinja2
  >>> from pdflatex2 import PDFLaTeX
  >>> from pathlib import Path
  >>> j2 = jinja2.Environment(
  ...     loader=jinja2.FileSystemLoader(Path(".")),
  ...     block_start_string=r"\BLOCK{",
  ...     block_end_string="}",
  ...     variable_start_string=r"\VAR{",
  ...     variable_end_string="}",
  ...     comment_start_string=r"\#{",
  ...     comment_end_string="}",
  ...     line_statement_prefix="%%",
  ...     line_comment_prefix="%#",
  ...     trim_blocks=True,
  ...     autoescape=True,
  ... )
  >>> template = j2.get_template("template.tex")
  >>> pdf = PDFLaTeX.from_jinja_template(template, key="value")
  >>> pdf.compile()

Copyright and License
=====================

SPDX-License-Identifier: `MIT <https://spdx.org/licenses/MIT.html>`_

pdflatex2, a Python/PDFLaTeX interface.

Copyright (C) 2022-2024 `Jeremy A Gray <gray@flyquackswim.com>`_.

Copyright (C) 2019 Marcelo Belo.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author
======

`Jeremy A Gray <gray@flyquackswim.com>`_
