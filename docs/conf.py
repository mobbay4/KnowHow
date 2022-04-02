# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'WG Know How'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',                              # to add a copybutton to code blocks
    'matplotlib.sphinxext.plot_directive',
    "sphinx_plotly_directive",
    'myst_parser',                                    # to import md in sphinx
    "sphinxcontrib.mermaid"                           # to render mermaid diagrams
]
master_doc = 'index'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- MyST configuration -------------------------------------------------------

myst_heading_anchors = 6
myst_enable_extensions = [
  "colon_fence",
  "dollarmath",
  "amsmath",
  "html_image"
]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = 'WG Know How'
html_show_sourcelink = True
show_navbar_depth = 3

# -- Extension configuration -------------------------------------------------

# -- Options for AutoDoc -----------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = False

# -- Options for InterSphinx -------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3.8', None)
}
