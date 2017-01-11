# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170109_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=128)),
                ('lname', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('bio', models.CharField(max_length=1280)),
                ('tagline', models.CharField(max_length=128)),
                ('image', models.FileField(upload_to='uploads/employee')),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.FileField(upload_to='uploads/food'),
        ),
    ]
