# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171009_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
    ]
