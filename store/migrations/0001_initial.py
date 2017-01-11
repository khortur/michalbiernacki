# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 11:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mattress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('width', models.IntegerField(default=90, validators=[django.core.validators.MinValueValidator(70), django.core.validators.MaxValueValidator(200)])),
                ('height', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(180), django.core.validators.MaxValueValidator(220)])),
                ('thickness', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(50)])),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
