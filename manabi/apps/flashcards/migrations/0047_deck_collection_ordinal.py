# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-02-10 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0046_drop_deck_priorities'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='collection_ordinal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]