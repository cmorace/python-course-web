Python-Course-Web
=================

Project for building a python course website with Sphinx.

To build the website, run the following:

.. code:: bash

   cd sphinx
   make clean
   make HTML
   python make_gh_pages.py

Then push changes to Github.

Dependencies
^^^^^^^^^^^^
pip install:

* sphinx
* nbsphinx
* sphinx_rtd_theme
* sphinx-intl
* nbsphinx_link
* ipython
* ipykernel

