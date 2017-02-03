# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-23 03:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0038_auto_20170123_0036'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='card',
            index_together=set([('owner', 'due_at', 'active', 'suspended')]),
        ),
    ]