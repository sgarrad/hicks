# -*- coding: utf-8 -*-
"""
Local settings
"""

from .common import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

