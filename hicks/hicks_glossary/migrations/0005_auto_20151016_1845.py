# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hicks_glossary', '0004_auto_20151012_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='definition',
            field=models.ForeignKey(related_name='terms', to='hicks_glossary.Definition'),
        ),
    ]
