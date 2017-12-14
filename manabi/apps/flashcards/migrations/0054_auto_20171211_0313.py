# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-11 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader_sources', '__first__'),
        ('flashcards', '0053_auto_20171123_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='example_sentence',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fact',
            name='reader_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facts', to='reader_sources.ReaderSource'),
        ),
    ]