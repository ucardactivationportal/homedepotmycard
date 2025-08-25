# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your modules are in another directory, add them here.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Manage Home Depot Credit Card'
copyright = '2025, Home Depot'
author = 'Home Depot Credit Services Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add Sphinx extensions here if needed
extensions = []

# Allow raw HTML in reStructuredText files
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme configuration (you can switch to another theme like 'sphinx_rtd_theme')
# html_theme = 'sphinx_rtd_theme'

# Basic metadata for the HTML output
html_title = "How I Handle My Home Depot Credit Card Without Hassle"
html_short_title = "Home Depot Card Management"
html_favicon = 'favicon.ico'  # Make sure to include this file in _static or root

# Hide the "View page source" link
html_show_sourcelink = False

# Allow unsafe raw HTML (used for buttons and links)
html_allow_unsafe = True

# Theme-specific options
html_theme_options = {
    'show_powered_by': False,
}

# Static files (like CSS, JS, images, favicon)
# Uncomment and set this if you have custom assets
# html_static_path = ['_static']
