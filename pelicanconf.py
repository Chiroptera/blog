#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Silva'
SITENAME = u'Random Access Knowledge'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8' # if ommited default is system locale
AUTHOR_BIO=""

# Blogroll
LINKS = (('Blog', 'http://rak.diogoaos.eu'),)
         #('About me', 'http://rak.diogaos.eu/Aboutme.html'),
         #('Archive', 'http://jinja.pocoo.org/'),)

# Social widget
"""
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
"""

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#output is the gh-pages repo
DELETE_OUTPUT_DIRECTORY = False 

DEFAULT_DATE_FORMAT = '%d %B %Y'
#DATE_FORMAT = {'en': '%d %B %Y'}

STATIC_PATHS = ['images']

THEME = "pelican-themes/pelican-svbtle"

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb']