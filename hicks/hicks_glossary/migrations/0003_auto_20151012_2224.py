# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('hicks_glossary', '0002_auto_20151011_2303'),
    ]

    operations = [
        migrations.RenameField(
            'Definition', 'definition', 'description'
        ),
    ]
