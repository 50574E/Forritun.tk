# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('forritun', '0003_auto_20150130_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='programminglanguage',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem'),
            preserve_default=True,
        ),
    ]
