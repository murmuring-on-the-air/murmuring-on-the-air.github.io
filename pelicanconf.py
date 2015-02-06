#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'the authors of MotA'
SITENAME = 'MotA'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Basic settings
ARTICLE_PATHS = ['changyuheng']
STATIC_PATHS = ['changyuheng']
DIRECT_TEMPLATES = ('index', 'authors', 'archives')
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

# - URL settings
ARTICLE_URL = 'post/{slug}/'
ARTICLE_SAVE_AS = 'post/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = 'page/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/folio/{number}/', '{base_name}/folio/{number}/index.html'),
)

# Plug-in settings
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
    'gravatar',
    'render_math',
]

# Theme
THEME = 'themes/pure'

# Theme pure
COVER_IMG_URL = 'http://i.imgur.com/rdpkAUi.jpg'
SOCIAL = (
    ('rss', 'feeds/all.atom.xml'),
)
