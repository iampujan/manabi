# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-01-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flashcards', '0035_inactive_decks_have_inactive_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedDeck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('deck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flashcards.Deck')),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
    ]