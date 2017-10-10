# -*- coding: utf-8 -*-
#
# F5 OpenStack Documentation documentation build configuration file, created by
# sphinx-quickstart on Thu Feb 18 15:51:54 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# import sys
# import os
# import os.path

import f5_sphinx_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'cloud_sptheme.ext.table_styling',
    'sphinxjp.themes.basicstrap',
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 OpenStack Solutions'
copyright = u'2017 F5 Networks Inc'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
# release = ''

# OpenStack release
openstack_release = "Newton"

rst_prolog = '''
.. raw:: html

   <script type="text/javascript">
    var home = "clouddocs.f5.com";
    var rtd = "f5-openstack-docs.readthedocs.io";

    if (window.location.hostname === rtd) {window.location.assign("http://" + home + "/cloud/openstack/v1");}
   </script>
'''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build',
                    'guides/includes',
                    'Thumbs.db',
                    '.DS_Store',
                    'drafts',
                    '_static/reuse'
                    ]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'f5_sphinx_theme'
html_theme_path = f5_sphinx_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
                        #'site_name': '',
                        'next_prev_link': False
                     }

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'F5 OpenStack Solutions'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'F5 OpenStack Home'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/f5-logo-solid-rgb_small.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = '_static/f5-logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5OpenStackDocumentationdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'F5OpenStackDocumentation.tex', u'F5 OpenStack Documentation',
     u'F5 Networks Inc', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'f5openstackdocumentation', u'F5 OpenStack Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5OpenStackDocumentation', u'F5 OpenStack Documentation',
     author, 'F5OpenStackDocumentation',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}

#intersphinx_mapping = {'heat': (
#    'http://f5-openstack-heat.readthedocs.io/en/master', None),
#    'heatplugins': (
#    'http://f5-openstack-heat-plugins.readthedocs.io/en/master', None),
#    'lbaasv2': (
#    'http://f5-openstack-lbaasv2-driver.readthedocs.io/en/master', None),
#    'agent': (
#    'http://f5-openstack-agent.readthedocs.io/en/master', None),
#    'f5sdk': (
#    'http://f5-sdk.readthedocs.io/en/latest/', None),
#    }

f5_lbaasv2_driver_shim_version = '10.1.0'
f5_lbaasv2_driver_shim_url = '\https://github.com/F5Networks/neutron-lbaas/releases/download/v%s/f5.tgz' % f5_lbaasv2_driver_shim_version
# F5 SDK release version should be set here
f5_sdk_version = '2.3.3'
# F5 icontrol REST version should be set here
f5_icontrol_version = '1.3.0'
version_latest = '10.1.0'


rst_epilog = '''
.. |agent-versions| replace:: 8.x, 9.x, 10.x
.. |heat-versions| replace:: 7.x, 8.x, 9.x, 10.x
.. |plugins-versions| replace:: 7.x, 8.x, 9.x, 10.x
.. |driver-versions| replace:: 8.x, 9.x, 10.x
.. |heat-t| replace:: F5 Heat template library
.. |agent-long| replace:: F5 Agent for OpenStack Neutron
.. |agent| replace:: F5 agent
.. |driver| replace:: F5 driver
.. |driver-long| replace:: F5 Driver for OpenStack LBaaSv2
.. |oslbaas| replace:: F5 Integration for OpenStack Neutron LBaaS
.. _OpenStack CLI: https://docs.openstack.org/cli-reference/
.. _OpenStack API: https://developer.openstack.org/api-guide/quick-start/index.html
.. |neutron| replace:: `OpenStack Neutron`_
.. |heat| replace:: `OpenStack Heat`_
.. _OpenStack Heat: https://docs.openstack.org/heat/latest
.. _OpenStack Neutron: https://docs.openstack.org/neutron/latest
.. _OpenStack Horizon: https://docs.openstack.org/horizon/latest
.. _OpenStack Barbican: https://docs.openstack.org/barbican/latest
.. _F5 Python SDK: http://f5-sdk.readthedocs.io/
.. _iControl REST: https://devcentral.f5.com/wiki/iControlrest.HomePage.ashx
.. |openstack| replace:: %(openstack_release)s
.. |f5_lbaasv2_driver_readme| raw:: html

   <a href="https://github.com/F5Networks/f5-openstack-lbaasv2-driver/blob/%(openstack_release_l)s/README.rst" target="_blank">README</a>
.. |f5_agent_readme| raw:: html
    
   <a href="https://github.com/F5Networks/f5-openstack-agent/blob/%(openstack_release_l)s/README.rst" target="_blank">README</a>
.. |neutron-lbaas| raw:: html
    
   <a href="https://docs.openstack.org/%(openstack_release_l)s/networking-guide/config-lbaas.html" target="_blank">Neutron LBaaS</a>
.. |os-deployment| raw:: html
    
   <a href="https://docs.openstack.org/%(openstack_release_l)s/networking-guide/deploy.html" target="_blank">OpenStack Deployment</a>
.. |os-extnet| raw:: html

    <a href="https://docs.openstack.org/%(openstack_release_l)s/install-guide-rdo/launch-instance-networks-provider.html" target+"_blank">external provider network</a>
.. _F5-Supported Heat Templates: /products/templates/openstack-heat/latest/index.html#f5-supported-heat-templates
.. _Better or Best license: https://f5.com/products/how-to-buy/simplified-licensing
.. |f5_lbaasv2_driver_shim_url| replace:: %(f5_lbaasv2_driver_shim_url)s
.. |community_tempest_lbaasv2_tests| raw:: html

   <a href="https://github.com/openstack/neutron-lbaas/tree/stable/%(openstack_release_l)s">tests</a>
.. |config-file| replace:: :agent:`configuration file <config-file.html>`
.. |configs| replace:: :agent:`configuration parameters <config-file.html#configuration-parameters>`
.. |env-generator| replace:: :driver:`F5 environment generator <environment-generator.html>`
.. |l2-seg| replace:: :agent:`L2 Segmentation Mode settings <config-file.html#l2-segmentation-mode-settings>`
.. |l3-seg| replace:: :agent:`L2 Segmentation Mode settings <config-file.html#l3-segmentation-mode-settings>`
.. |grm| replace:: :agent:`Global routed mode <global-routed-mode.html>`
.. |l2mode| replace:: :agent:`L2-adjacent mode <l2-adjacent-mode.html>`
.. |driver-settings| replace:: :agent:`Device driver\/iControl Driver settings <device-driver-settings.html>`
.. _Device driver/iControl Driver settings: /products/openstack/agent/latest/device-driver-settings.html
.. |f5_agent_pip_url_branch| replace:: git+https://github.com/F5Networks/f5-openstack-agent@%(openstack_release_l)s
.. |f5_agent_deb_url| replace:: \https://github.com/F5Networks/f5-openstack-agent/releases/download/v%(version_latest)s/python-f5-openstack-agent_%(version_latest)s-1_1404_all.deb
.. |f5_agent_rpm_url| replace:: \https://github.com/F5Networks/f5-openstack-agent/releases/download/v%(version_latest)s/f5-openstack-agent-%(version_latest)s-1.el7.noarch.rpm
.. |f5_agent_deb_package| replace:: python-f5-openstack-agent_%(version_latest)s-1_1404_all.deb
.. |f5_agent_rpm_package| replace:: f5-openstack-agent-%(version_latest)s-1.el7.noarch.rpm
.. |f5_sdk_deb_url| replace:: \https://github.com/F5Networks/f5-common-python/releases/download/v%(f5_sdk_version)s/python-f5-sdk_%(f5_sdk_version)s-1_1404_all.deb
.. |f5_sdk_rpm_url| replace:: \https://github.com/F5Networks/f5-common-python/releases/download/v%(f5_sdk_version)s/f5-sdk-%(f5_sdk_version)s-1.el7.noarch.rpm
.. |f5_sdk_rpm_package| replace:: f5-sdk-%(f5_sdk_version)s-1.el7.noarch.rpm
.. |f5_sdk_deb_package| replace:: python-f5-sdk_%(f5_sdk_version)s-1_1404_all.deb
.. |f5_icontrol_deb_url| replace:: \https://github.com/F5Networks/f5-icontrol-rest-python/releases/download/v%(f5_icontrol_version)s/python-f5-icontrol-rest_%(f5_icontrol_version)s-1_1404_all.deb
.. |f5_icontrol_rpm_url| replace:: \https://github.com/F5Networks/f5-icontrol-rest-python/releases/download/v%(f5_icontrol_version)s/f5-icontrol-rest-%(f5_icontrol_version)s-1.el7.noarch.rpm
.. |f5_icontrol_rpm_package| replace:: f5-icontrol-rest-%(f5_icontrol_version)s-1.el7.noarch.rpm
.. |f5_icontrol_deb_package| replace:: python-f5-icontrol-rest_%(f5_icontrol_version)s-1_1404_all.deb
.. |f5_lbaasv2_driver_pip_url_branch| replace:: git+https:\//github.com/F5Networks/f5-openstack-lbaasv2-driver@%(openstack_release_l)s
.. |f5_lbaasv2_driver_deb_url| replace:: \https://github.com/F5Networks/f5-openstack-lbaasv2-driver/releases/download/v%(version_latest)s/python-f5-openstack-lbaasv2-driver_%(version_latest)s-1_1404_all.deb
.. |f5_lbaasv2_driver_rpm_url| replace:: \https://github.com/F5Networks/f5-openstack-lbaasv2-driver/releases/download/v%(version_latest)s/f5-openstack-lbaasv2-driver-%(version_latest)s-1.el7.noarch.rpm
.. |f5_lbaasv2_driver_deb_package| replace:: python-f5-openstack-lbaasv2-driver_%(version_latest)s-1_1404_all.deb
.. |f5_lbaasv2_driver_rpm_package| replace:: f5-openstack-lbaasv2-driver-%(version_latest)s-1.el7.noarch.rpm
.. |f5_agent_pip_url| replace:: git+https://github.com/F5Networks/f5-openstack-agent@v%(version_latest)s
.. |f5_driver_pip_url| replace:: git+https://github.com/F5Networks/f5-openstack-lbaasv2-driver@v%(version_latest)s
.. |version_latest| replace:: %(version_latest)s
.. _Configure the F5 Agent for OpenStack Neutron: /products/openstack/agent/latest/index.html#configure-the-f5-openstack-agent
.. _HPE Helion OpenStack: https://docs.hpcloud.com/hrc/helionReady.html
.. _Mirantis OpenStack: https://www.mirantis.com/partners/f5-networks/
.. _RedHat OpenStack Platform: https://access.redhat.com/ecosystem/software/1446683
.. _OpenStack Nova: https://docs.openstack.org/nova/latest
.. _Install the F5 LBaaSv2 Driver: /products/openstack/f5-openstack-lbaasv2-driver/latest/index.html#installation
.. _Install the F5 Agent: /products/openstack/f5-openstack-agent/latest/index.html#installation
''' % {
  'openstack_release': openstack_release,
  'openstack_release_l': openstack_release.lower(),
  'f5_lbaasv2_driver_shim_url': f5_lbaasv2_driver_shim_url,
  'f5_sdk_version': f5_sdk_version,
  'f5_icontrol_version': f5_icontrol_version,
  'version_latest': version_latest,
  'version': version
}

# Markup to shorten links to external sites
extlinks = {'agent': ('http://clouddocs.f5.com/products/openstack/agent/latest/%s',
                      ''),
            'driver': ('http://clouddocs.f5.com/products/openstack/lbaasv2-driver/latest/%s',
            ''),
            'heat': ('http://clouddocs.f5.com/products/templates/openstack-heat/latest/%s',
            ''),
            'plugins': ('http://clouddocs.f5.com/products/openstack/heat-plugins/latest/%s',
            ''),
            'github': ('https://github.com/f5networks/%s',
            '')
}

# Ignore anchors when running linkcheck
linkcheck_anchors = False
