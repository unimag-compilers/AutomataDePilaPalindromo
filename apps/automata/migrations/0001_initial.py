# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=30, unique=True)),
                ('isPalindrome', models.CharField(choices=[(0, 'Unknown'), (1, 'Yes'), (2, 'No')], default=0, max_length=1)),
                ('automata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automata.Automata')),
            ],
        ),
    ]