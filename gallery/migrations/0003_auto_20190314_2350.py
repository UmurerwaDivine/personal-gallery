# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190314_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]