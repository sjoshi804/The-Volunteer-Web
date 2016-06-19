# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NGODomains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NGOEmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.TextField(blank=True, max_length=100)),
                ('position', models.TextField(max_length=50)),
                ('admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NGOProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_id', models.TextField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=100)),
                ('ngo_name', models.TextField(max_length=100)),
                ('ngo_description', models.TextField(blank=True, max_length=200)),
                ('ngo_domain', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=100)),
                ('skill_science', models.IntegerField(default=0)),
                ('skill_math', models.IntegerField(default=0)),
                ('skill_english', models.IntegerField(default=0)),
                ('skill_ict', models.IntegerField(default=0)),
                ('skill_programming', models.IntegerField(default=0)),
                ('skill_socialmediamarket', models.IntegerField(default=0)),
                ('skill_sport', models.IntegerField(default=0)),
                ('interests', models.ManyToManyField(to='Registration.NGODomains')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
