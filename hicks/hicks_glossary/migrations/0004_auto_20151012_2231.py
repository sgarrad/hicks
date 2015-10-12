# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hicks_glossary', '0003_auto_20151012_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='description',
            field=models.TextField(verbose_name=b'Description'),
        ),
    ]
