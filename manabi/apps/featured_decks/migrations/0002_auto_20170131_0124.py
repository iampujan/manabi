# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-31 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('featured_decks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureddeck',
            name='item_content_type',
            field=models.ForeignKey(default=44, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featureddeck',
            name='item_id',
            field=models.PositiveIntegerField(default=380),
            preserve_default=False,
        ),
    ]