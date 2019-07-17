# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-16 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(related_name='artists', to='first_app.Song'),
        ),
    ]
