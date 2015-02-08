# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('forritun', '0004_auto_20150130_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedWithCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(verbose_name='Content type', related_name='forritun_taggedwithcategory_tagged_items', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagWithCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100, unique=True)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=100, unique=True)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taggedwithcategory',
            name='tag',
            field=models.ForeignKey(related_name='forritun_taggedwithcategory_items', to='forritun.TagWithCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programminglanguage',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='forritun.TaggedWithCategory', to='forritun.TagWithCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='forritun.TaggedWithCategory', to='forritun.TagWithCategory'),
            preserve_default=True,
        ),
    ]
