# Overview

This is a simple module to execute pdflatex in an easy and clean way.
The pdflatex command line utility by default generates a lot of output and can create many files.

## Instantiation

The PDFLaTeX class can be instantiated directly or through helpers:

- **from_texfile(filename)**
- **from_binarystring(binstr, jobname)**
- **from_jinja2_template(jinja2_template, jobname = None, \*\*render_kwargs)**

jobname is any string that can be used to create a valid filename;


## Examples:

In all the following examples, no files are left on the filesystem,
unless requested with the *keep_pdf_file* and *keep_log_file* parameters
to the *create_pdf* method.

### Create PDF from .tex file

    from pdflatex import PDFLaTeX

    pdfl = PDFLaTeX.from_texfile('my_file.tex')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

The function **create_pdf** returns 3 results:
1. The pdf file in a binary string;
2. The log file generated by pdflatex as text;
3. An instance of subprocess.CompleteProcess with the results of the pdflatex execution.

Also, **create_pdf** takes a few parameters:
1. keep_pdf_file: an optional boolean. Default to False. If True a pdf file is maintained. Its location and name depends on the value of the -output-directory and -jobname parameters. It is also derived from the tex filename or the jinja2 template filename if no parameter is given;
2. keep_log_file: same thing, for the log file.
3. env: a default ENV mapping for the execution of pdflatex. You probably want to skip this.


### Create PDF from Jinja2 Template

    import os
    import pdflatex
    import jinja2 
    
    env = pdflatex.JINJA2_ENV
    env['loader'] = jinja2.FileSystemLoader(os.path.abspath('.'))
    env = jinja2.Environment(**env)
    template = env.get_template('jinja.tex')
    pdfl = pdflatex.PDFLaTeX.from_jinja2_template(template, data='Hello world!')
    pdf, log, cp = pdfl.create_pdf()

Quite self explanatory, just note that pdflatex includes a dictionary
JINJA2_ENV with a suggestion of environment parameters for you to use with
jinja2 and LaTeX. It os defined as:

    JINJA2_ENV = {'block_start_string': '\BLOCK{',
                  'block_end_string': '}',
                  'variable_start_string': '\VAR{',
                  'variable_end_string': '}',
                  'comment_start_string': '\#{',
                  'comment_end_string': '}',
                  'line_statement_prefix': '%%',
                  'line_comment_prefix': '%#',
                  'trim_blocks': True,
                  'autoescape': False }


### Create PDF file from binary string:

    import pdflatex

    with open('my_file.tex', 'rb') as f:
        pdfl = pdflatex.PDFLaTeX.from_binarystring(f.read(), 'my_file')
    pdf, log, cp = pdfl.create_pdf()