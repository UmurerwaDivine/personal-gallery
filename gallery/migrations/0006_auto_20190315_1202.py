# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20190315_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery/s'),
        ),
    ]
