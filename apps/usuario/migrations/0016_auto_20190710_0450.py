# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-10 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_merge_20190710_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(default='fotos_perfil/no-profile-picture.jpg', upload_to='fotos_perfil'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
