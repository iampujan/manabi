# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0020_auto_20160903_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardhistory',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='cardhistory',
            name='question_duration',
        ),
    ]