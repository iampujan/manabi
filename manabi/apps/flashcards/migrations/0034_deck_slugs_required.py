# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-12-03 21:28
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0033_prefill_deck_slug_redux_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=b'name'),
        ),
    ]