# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=50)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('language', models.ForeignKey(to='forritun.ProgrammingLanguage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
