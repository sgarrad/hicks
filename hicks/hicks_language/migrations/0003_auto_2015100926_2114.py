# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_data(apps, schema_editor):
    Language = apps.get_model('hicks_language', 'Language')
    Language(code='en-GB', display_name='English (United Kingdom)').save()



class Migration(migrations.Migration):
    dependencies = [
        ('hicks_language', '0002_auto_20151009_1529'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
