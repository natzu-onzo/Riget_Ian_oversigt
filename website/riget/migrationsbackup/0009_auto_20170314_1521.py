# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-14 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riget', '0008_fet_persons_fet_persons_deleted_fet_record_images_fet_records_fet_records_deleted_fet_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FET_records',
        ),
        migrations.DeleteModel(
            name='FET_records_deleted',
        ),
    ]
