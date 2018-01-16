# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(serialize=False, primary_key=True)),
                ('pregunta', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'pregunta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelPregunta',
            fields=[
                ('id_relp', models.AutoField(serialize=False, primary_key=True)),
                ('tipo', models.CharField(max_length=10)),
                ('clase', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'rel_pregunta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_resp', models.AutoField(serialize=False, primary_key=True)),
                ('calificacion', models.IntegerField(null=True, blank=True)),
                ('texto', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'db_table': 'respuesta',
                'managed': False,
            },
        ),
    ]
