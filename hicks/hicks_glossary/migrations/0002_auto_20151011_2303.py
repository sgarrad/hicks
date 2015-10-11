# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hicks_glossary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='project',
            field=models.ForeignKey(related_name='definitions', to='hicks_glossary.Project'),
        ),
    ]
