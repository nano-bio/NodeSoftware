# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0008_species_inchikey_positive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='inchikey_negative',
            field=models.CharField(blank=True, db_index=True, max_length=27, verbose_name='InChI-Key anion'),
        ),
        migrations.AlterField(
            model_name='species',
            name='inchikey_neutral',
            field=models.CharField(blank=True, db_index=True, max_length=27, verbose_name='InChI-Key neutral'),
        ),
        migrations.AlterField(
            model_name='species',
            name='inchikey_positive',
            field=models.CharField(blank=True, db_index=True, max_length=27, verbose_name='InChI-Key cation'),
        ),
    ]