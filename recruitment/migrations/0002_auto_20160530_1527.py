# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='mid',
        ),
        migrations.RemoveField(
            model_name='companyjob',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companyjob',
            name='job_deliver',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='category',
        ),
        migrations.RemoveField(
            model_name='jobdeliver',
            name='category',
        ),
        migrations.RemoveField(
            model_name='jobwanted',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='jobwanted',
            name='job_deliver',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mid',
        ),
        migrations.RemoveField(
            model_name='usercv',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='usercv',
            name='user',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='CompanyJob',
        ),
        migrations.DeleteModel(
            name='CV',
        ),
        migrations.DeleteModel(
            name='JobCategory',
        ),
        migrations.DeleteModel(
            name='JobDeliver',
        ),
        migrations.DeleteModel(
            name='JobWanted',
        ),
        migrations.DeleteModel(
            name='Manage',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserCV',
        ),
    ]
