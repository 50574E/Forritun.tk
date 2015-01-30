# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forritun', '0002_auto_20150125_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
