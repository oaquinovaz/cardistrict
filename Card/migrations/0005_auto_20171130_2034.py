# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card', '0004_auto_20171130_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enciclopedia',
            name='categoria',
            field=models.CharField(choices=[('Spreads', 'Spreads'), ('Two-Handed Cuts', 'Two-Handed Cuts'), ('Utilities', 'Utilities'), ('Twirls', 'Twirls'), ('Isolations', 'Isolations'), ('One-Handed Cuts', 'One-Handed Cuts'), ('One-Handed Fans', 'One-Handed Fans'), ('Two-Handed Fans', 'Two-Handed Fans'), ('Grips', 'Grips'), ('Shuffles', 'Shuffles')], max_length=16),
        ),
        migrations.AlterField(
            model_name='identificarmovimiento',
            name='nombreIMovimiento',
            field=models.CharField(max_length=50),
        ),
    ]