# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-24 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conductor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Concepcion', max_length=40)),
                ('direccion', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Paradas',
                'verbose_name': 'Parada',
            },
        ),
        migrations.CreateModel(
            name='Tramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_en_viaje', models.IntegerField(blank=True, null=True)),
                ('hora_salida', models.CharField(default='15:00', max_length=30)),
                ('hora_llegada', models.CharField(default='15:00', max_length=30)),
                ('fecha', models.CharField(default='21/10/18', max_length=30)),
                ('asientos_disponibles', models.IntegerField(blank=True, null=True)),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ParadaDestino', to='viaje.Parada')),
                ('origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ParadaOrigen', to='viaje.Parada')),
            ],
            options={
                'verbose_name_plural': 'Tramos',
                'verbose_name': 'Tramo',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('estado', models.CharField(max_length=20)),
                ('porta_maleta', models.BooleanField(default=False)),
                ('silla_niños', models.BooleanField(default=False)),
                ('mascotas', models.BooleanField(default=False)),
                ('tarifaPreferencias', models.IntegerField(blank=True, null=True)),
                ('max_personas_atras', models.IntegerField(blank=True, null=True)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conductor.Conductor')),
                ('tramos', models.ManyToManyField(to='viaje.Tramo')),
            ],
            options={
                'verbose_name_plural': 'Viajes',
                'verbose_name': 'Viaje',
            },
        ),
    ]
