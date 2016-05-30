# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20160530_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('establish', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('property', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('scale', models.CharField(max_length=20)),
                ('intro', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyJob',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('company', models.ForeignKey(to='recruitment.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=20)),
                ('work_exp', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('intro', models.TextField(max_length=300)),
                ('expected_job', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('cate_name', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('pre_cate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobDeliver',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('job_name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=40)),
                ('numb', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('work_year', models.CharField(max_length=5)),
                ('age', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('contact', models.CharField(max_length=20)),
                ('created_time', models.CharField(max_length=20)),
                ('category', models.ForeignKey(to='recruitment.JobCategory')),
            ],
        ),
        migrations.CreateModel(
            name='JobWanted',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('result', models.CharField(max_length=10)),
                ('cv', models.ForeignKey(to='recruitment.CV')),
                ('job_deliver', models.ForeignKey(to='recruitment.JobDeliver')),
            ],
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('ID', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('role', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('mid', models.ForeignKey(to='recruitment.Manage')),
            ],
        ),
        migrations.CreateModel(
            name='UserCV',
            fields=[
                ('ID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('cv', models.ForeignKey(to='recruitment.CV')),
                ('user', models.ForeignKey(to='recruitment.User')),
            ],
        ),
        migrations.AddField(
            model_name='cv',
            name='category',
            field=models.ForeignKey(to='recruitment.JobCategory'),
        ),
        migrations.AddField(
            model_name='companyjob',
            name='job_deliver',
            field=models.ForeignKey(to='recruitment.JobDeliver'),
        ),
        migrations.AddField(
            model_name='company',
            name='mid',
            field=models.ForeignKey(to='recruitment.Manage'),
        ),
    ]
