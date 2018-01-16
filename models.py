# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Conferencia(models.Model):
    id_conf = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey('Evento', db_column='id_evento')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    nombre_pon = models.CharField(max_length=100)
    path_imgc = models.CharField(max_length=100)
    fecha = models.DateField()
    def __unicode__(self):
              return self.nombre
    class Meta:
        managed = False
        db_table = 'conferencia'


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    lugar = models.CharField(max_length=150)
    fecha_in = models.DateField()
    fecha_fin = models.DateField()
    path_img = models.CharField(max_length=100)
    def __unicode__(self):
              return self.nombre
    class Meta:
        managed = False
        db_table = 'evento'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=150)
    def __unicode__(self):
              return self.pregunta
    class Meta:
        managed = False
        db_table = 'pregunta'


class RelPregunta(models.Model):
    id_relp = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey(Pregunta, db_column='id_pregunta')
    id_conf = models.ForeignKey(Conferencia, db_column='id_conf', blank=True, null=True)
    id_evento = models.ForeignKey(Evento, db_column='id_evento', blank=True, null=True)
    tipo = models.CharField(max_length=10)
    clase = models.CharField(max_length=10)
   
    class Meta:
        managed = False
        db_table = 'rel_pregunta'


class RelUe(models.Model):
    id_rel_ue = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', db_column='id_usuario')
    id_evento = models.ForeignKey(Evento, db_column='id_evento')
    estatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rel_ue'


class Respuesta(models.Model):
    id_resp = models.AutoField(primary_key=True)
    id_rel_ue = models.ForeignKey(RelUe, db_column='id_rel_ue')
    id_relp = models.ForeignKey(RelPregunta, db_column='id_relp')
    calificacion = models.IntegerField(blank=True, null=True)
    texto = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    fecha_reg = models.DateField()

    class Meta:
        managed = False
        db_table = 'usuario'
