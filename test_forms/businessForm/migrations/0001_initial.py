# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mission_statement', models.CharField(max_length=1000)),
                ('incorpDate', models.DateField()),
                ('files', models.FileField(upload_to='')),
            ],
        ),
    ]
