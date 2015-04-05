#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Silva'
SITENAME = u'Random Access Knowledge'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

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
RELATIVE_URLS = False

#output is the gh-pages repo
DELETE_OUTPUT_DIRECTORY = False 

DEFAULT_DATE_FORMAT = '%a %d %B %Y'

STATIC_PATHS = ['images']

THEME = "pelican-themes/pelican-svbtle"