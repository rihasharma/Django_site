# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_project_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
