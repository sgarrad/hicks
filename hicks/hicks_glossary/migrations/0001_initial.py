# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hicks_language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('definition', models.TextField(verbose_name=b'Definition')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b'Name')),
                ('slug', models.SlugField()),
                ('base_language', models.ForeignKey(related_name='project_base_language', to='hicks_language.Language')),
                ('supported_languages', models.ManyToManyField(to='hicks_language.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.TextField(verbose_name=b'Term')),
                ('definition', models.ForeignKey(related_name='term_definition', to='hicks_glossary.Definition')),
                ('language', models.ForeignKey(related_name='term_language', to='hicks_language.Language')),
            ],
        ),
        migrations.AddField(
            model_name='definition',
            name='project',
            field=models.ForeignKey(to='hicks_glossary.Project'),
        ),
    ]
