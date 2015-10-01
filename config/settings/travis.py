# -*- coding: utf-8 -*-
"""
Local settings
"""
import os
from .common import *  # noqa

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'hicks',
            'USER': 'postgres',
        }
    }