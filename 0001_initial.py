# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id_conf', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=150)),
                ('nombre_pon', models.CharField(max_length=100)),
                ('path_imgc', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'conferencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=150)),
                ('lugar', models.CharField(max_length=150)),
                ('fecha_in', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('path_img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_pregunta', models.IntegerField()),
                ('pregunta', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'preguntas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelPreguntas',
            fields=[
                ('id_relp', models.AutoField(serialize=False, primary_key=True)),
                ('tipo', models.CharField(max_length=10)),
                ('clase', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'rel_preguntas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelUe',
            fields=[
                ('id_rel_ue', models.AutoField(serialize=False, primary_key=True)),
                ('estatus', models.IntegerField()),
            ],
            options={
                'db_table': 'rel_ue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id_resp', models.AutoField(serialize=False, primary_key=True)),
                ('calificacion', models.IntegerField(null=True, blank=True)),
                ('texto', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'db_table': 'respuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('fecha_reg', models.DateField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
