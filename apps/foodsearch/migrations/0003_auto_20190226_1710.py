# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsearch', '0002_auto_20190226_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.TextField(),
        ),
    ]