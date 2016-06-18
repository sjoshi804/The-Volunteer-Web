# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.TextField(max_length=100)),
                ('sender', models.TextField(blank=True, max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('purpose', models.TextField(max_length=1000)),
                ('status', models.TextField(default=b'Pending', max_length=240)),
                ('invoice_img', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Offline_Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.TextField(max_length=100)),
                ('donor_name', models.TextField(blank=True, max_length=100)),
                ('amount_donated', models.PositiveIntegerField()),
                ('cause', models.TextField(blank=True, max_length=1000)),
                ('mode_of_payment', models.TextField(default=b'Not Specified', max_length=30)),
                ('date_donated', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offline_Vol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_req', models.DateTimeField(auto_now_add=True, null=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('volunteer_name', models.TextField(blank=True, max_length=100)),
                ('date_vol', models.DateField(blank=True, null=True)),
                ('time_vol', models.TimeField(blank=True)),
                ('hours_vol', models.PositiveSmallIntegerField()),
                ('activity', models.TextField(max_length=100)),
            ],
        ),
    ]
