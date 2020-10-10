Python-Course-Web
=================

Project for building a python course website with Sphinx.

to build, run:

.. code:: bash

   make html

Then run the `make_gh_pages.py` script to transfer build files to gh_pages directory.

`make_gh_pages.py` creates the correct directory structure and documents needed to host the page on gihub pages.


Dependencies
^^^^^^^^^^^^
* sphinx
* nbsphinx
* sphinx_rtd_theme
* sphinx-itl