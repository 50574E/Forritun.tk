# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forritun', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programminglanguage',
            name='slug',
            field=models.SlugField(default='forritunarmal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=models.SlugField(default='resource'),
            preserve_default=False,
        ),
    ]
