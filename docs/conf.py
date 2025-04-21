
import os
import sphinx_rtd_theme

project = 'GRACE-FO'
copyright = '2025, GRACE-FO'
release = '2025'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx','sphinx.ext.autosectionlabel']

templates_path = ['_templates']
exclude_patterns = []


# Detect RTD project to set master_doc
rtd_project = os.environ.get('READTHEDOCS_PROJECT')

if rtd_project == 'l1':
    master_doc = 'L1/index'
elif rtd_project == 'l2':
    master_doc = 'L2/index'
else:
    master_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "_static/GRACE_FO_logo.png"
html_theme_options = {
    'logo_only': True,
	'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}