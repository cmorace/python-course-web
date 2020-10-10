"""A script to move sphinx build files to a gh-pages directory.

-------------------------------------------------------------------------------
Github pages looks for an index.html in either the root directory or a
"root/docs/" directory of a specific branch. This script copies the build files
generated my sphinx's `make html` command in the main branch to a gh-pages
directory in the gh-pages branch.

Assumes the following project directory structure

project root folder
|
|_ gh_pages (gh_pages branch)
|    |
|    |_ docs/
|
|_ sphinx (main branch)
     |
     |_ build
     |    |
     |    |_html/
     |
     |_ make_gh_pages.py

We also add an empty `.nojekyll` file to let Github pages know this is not a
jekyll project.
"""

from os.path import dirname, abspath
from shutil import copytree, rmtree

sphinx_dir = dirname(abspath(__file__))
gh_pages_docs_dir = dirname(sphinx_dir) + '/docs/'
sphinx_build_dir = sphinx_dir + "/build/html/"
rmtree(gh_pages_docs_dir, ignore_errors=True)
copytree(sphinx_build_dir, gh_pages_docs_dir)
open(gh_pages_docs_dir + '.nojekyll', 'a').close()
