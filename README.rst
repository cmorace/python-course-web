Python-Course-Web
=================

Project for building a python course website with Sphinx.

To build the website, run the following:

.. code:: bash

   cd sphinx
   make clean
   make html
   python make_github_pages.py

then push changes to github.

Dependencies
^^^^^^^^^^^^
pip install:

* sphinx
* nbsphinx
* sphinx_rtd_theme
* sphinx-itl
