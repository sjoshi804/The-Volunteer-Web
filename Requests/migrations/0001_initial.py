# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityname', models.TextField(default=b'', max_length=240)),
                ('skill_science', models.BooleanField(default=False)),
                ('skill_math', models.BooleanField(default=False)),
                ('skill_english', models.BooleanField(default=False)),
                ('skill_ict', models.BooleanField(default=False)),
                ('skill_programming', models.BooleanField(default=False)),
                ('skill_socialmediamarket', models.BooleanField(default=False)),
                ('skill_sport', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_req', models.DateTimeField(auto_now_add=True, null=True)),
                ('event_name', models.TextField(default=b'', max_length=30)),
                ('organizer', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True, null=True)),
                ('enddate_vol', models.DateField(blank=True, null=True)),
                ('starttime_vol', models.TimeField(blank=True)),
                ('endtime_vol', models.TimeField(blank=True)),
                ('activity_goal', models.TextField(max_length=240, null=True)),
                ('status', models.TextField(default=b'Upcoming')),
                ('activities', models.ManyToManyField(to='Requests.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_req', models.DateTimeField(auto_now_add=True, null=True)),
                ('project_name', models.TextField(default=b'', max_length=30)),
                ('organizer', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True, null=True)),
                ('enddate_vol', models.DateField(blank=True, null=True)),
                ('starttime_vol', models.TimeField(blank=True)),
                ('endtime_vol', models.TimeField(blank=True)),
                ('activities', models.TextField(default=b'', max_length=240)),
                ('status', models.TextField(default=b'Upcoming')),
            ],
        ),
        migrations.CreateModel(
            name='Recurring_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField(max_length=20)),
                ('recepient', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True, null=True)),
                ('enddate_vol', models.DateField(blank=True, null=True)),
                ('time_vol', models.TimeField(blank=True)),
                ('activity', models.TextField(default=b'', max_length=240)),
                ('frequency', models.TextField(default=b'', max_length=240)),
                ('date_time_req', models.DateTimeField(auto_now_add=True, null=True)),
                ('vol_duration', models.IntegerField(default=0)),
                ('status', models.TextField(default=b'Pending')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer_ngo_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_req', models.DateTimeField(auto_now_add=True, null=True)),
                ('sender', models.TextField(max_length=20)),
                ('recepient', models.TextField(max_length=20)),
                ('date_vol', models.DateField(blank=True, null=True)),
                ('time_vol', models.TimeField(blank=True)),
                ('activity', models.TextField(default=b'', max_length=240)),
                ('vol_duration', models.IntegerField(default=0)),
                ('status', models.TextField(default=b'Pending')),
                ('feedback_user', models.TextField(blank=True, default=b'', max_length=240)),
                ('feedback_ngo', models.TextField(blank=True, default=b'', max_length=240)),
                ('feedback_userrating', models.IntegerField(default=0)),
                ('feedback_ngorating', models.IntegerField(default=0)),
                ('ngo_complete', models.BooleanField(default=False)),
                ('onetime', models.BooleanField(default=True)),
            ],
        ),
    ]
