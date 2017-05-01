# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=25)),
                ('periodicidad', models.CharField(max_length=12)),
            ],
        ),
    ]
