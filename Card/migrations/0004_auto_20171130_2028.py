# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card', '0003_auto_20171130_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enciclopedia',
            name='categoria',
            field=models.CharField(choices=[('Grips', 'Grips'), ('One-Handed Cuts', 'One-Handed Cuts'), ('Shuffles', 'Shuffles'), ('One-Handed Fans', 'One-Handed Fans'), ('Utilities', 'Utilities'), ('Spreads', 'Spreads'), ('Two-Handed Fans', 'Two-Handed Fans'), ('Two-Handed Cuts', 'Two-Handed Cuts'), ('Isolations', 'Isolations'), ('Twirls', 'Twirls')], max_length=16),
        ),
    ]