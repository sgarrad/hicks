# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text=b'http://www.w3.org/International/articles/language-tags', unique=True, max_length=50, verbose_name=b'Code')),
                ('display_name', models.CharField(max_length=255, verbose_name=b'Display Name')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
