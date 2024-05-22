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

===============================
 pdflatex Command Line Options
===============================

Version::

  MiKTeX-pdfTeX 4.19 (MiKTeX 24.3.31)

Options::

  Usage: pdflatex [OPTION...] [COMMAND...]
      -alias=APP                      Pretend to be APP.  This affects both the
                                      format used and the search path.
      -aux-directory=DIR              Use DIR as the directory to write
                                      auxiliary files to.
      -buf-size=N                     Set buf_size to N.
      -c-style-errors                 Enable file:line:error style messages.
      -disable-8bit-chars             Make only 7-bit characters printable.
      -disable-installer              Disable the package installer.  Missing
                                      files will not be installed.
      -disable-write18                Disable the \write18{COMMAND} construct.
      -dont-parse-first-line          Do not parse the first line of the input
                                      line to look for a dump name and/or extra
                                      command-line options.
      -draftmode                      Switch on draft mode (generates no output).
      -enable-8bit-chars              Make all characters printable by default.
      -enable-enctex                  Enable EncTeX extensions such as \mubyte.
      -enable-etex                    Enable e-TeX extensions.
      -enable-installer               Enable the package installer.  Missing
                                      files will be installed.
      -enable-mltex                   Enable MLTeX extensions such as
                                      \charsubdef.
      -enable-write18                 Enable the \write18{COMMAND} construct.
      -error-line=N                   Set error_line to N.
      -extra-mem-bot=N                Set extra_mem_bot to N.
      -extra-mem-top=N                Set extra_mem_top to N.
      -font-max=N                     Set font_max to N.
      -font-mem-size=N                Set font_mem_size to N.
      -half-error-line=N              Set half_error_line to N.
      -halt-on-error                  Stop after the first error.
      -hash-extra=N                   Set hash_extra to N.
      -help                           Show this help screen and exit.
      -include-directory=DIR          Prefix DIR to the input search path.
      -initialize                     Be the INI variant of the program.
      -interaction=MODE               Set the interaction mode; MODE must be one
                                      of: batchmode, nonstopmode, scrollmode,
                                      errorstopmode.
      -job-name=NAME                  Set the job name and hence the name(s) of
                                      the output file(s).
      -job-time=FILE                  Set the job time.  Take FILE's timestamp
                                      as the reference.
      -main-memory=N                  Set main_memory to N.
      -max-in-open=N                  Set max_in_open to N.
      -max-print-line=N               Set max_print_line to N.
      -max-strings=N                  Set max_strings to N.
      -nest-size=N                    Set nest_size to N.
      -no-c-style-errors              Disable file:line:error style messages.
      -output-directory=DIR           Use DIR as the directory to write output
                                      files to.
      -output-format=FORMAT           Set the output format.
      -param-size=N                   Set param_size to N.
      -parse-first-line               Parse the first line of the input line to
                                      look for a dump name and/or extra
                                      command-line options.
      -pool-free=N                    Set pool_free to N.
      -pool-size=N                    Set pool_size to N.
      -quiet                          Suppress all output (except errors).
      -record-package-usages=FILE     Enable the package usage recorder.  Output
                                      is written to FILE.
      -recorder                       Turn on the file name recorder to leave a
                                      trace of the files opened for input and
                                      output in a file with extension .fls.
      -restrict-write18               Partially enable the \write18{COMMAND}
                                      construct.
      -save-size=N                    Set save_size to N.
      -src-specials                   Insert source specials in certain places
                                      of the DVI file.
      -stack-size=N                   Set stack_size to N.
      -string-vacancies=N             Set string_vacancies to N.
      -synctex=N                      Generate SyncTeX data for previewers if
                                      nonzero.
      -tcx=TCXNAME                    Use the TCXNAME translation table to set
                                      the mapping of input characters and
                                      re-mapping of output characters.
      -time-statistics                Show processing time statistics.
      -trace=OPTIONS                  Turn tracing on.  OPTIONS must be a
                                      comma-separated list of trace options.
                                      See the manual, for more information.
      -trie-size=N                    Set trie_size to N.
      -undump=NAME                    Use NAME instead of program name when
                                      loading internal tables.
      -verbose                        Turn on verbose mode.
      -version                        Print version information and exit.
