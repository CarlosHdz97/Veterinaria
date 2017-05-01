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
            name='Cliente',
            fields=[
                ('rfc', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
