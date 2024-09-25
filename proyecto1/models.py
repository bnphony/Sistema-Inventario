# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True)
    nombre_cur = models.CharField(max_length=100, blank=True, null=True)
    descripcion_cur = models.CharField(max_length=300, blank=True, null=True)
    horas_cur = models.IntegerField(blank=True, null=True)
    precio_cur = models.FloatField(blank=True, null=True)
    fecha_inicio_cur = models.CharField(max_length=30, blank=True, null=True)
    fecha_final_cur = models.CharField(max_length=30, blank=True, null=True)
    cupos_cur = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class CursoProfesor(models.Model):
    id_cur_prof = models.AutoField(primary_key=True)
    fk_id_cur_prof = models.ForeignKey(Curso, models.DO_NOTHING, db_column='fk_id_cur_prof', blank=True, null=True)
    fk_id_prof_prof = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='fk_id_prof_prof', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso_profesor'


class Inscripcion(models.Model):
    id_ins = models.AutoField(primary_key=True)
    fecha_ins = models.CharField(max_length=30, blank=True, null=True)
    estado_ins = models.CharField(max_length=30, blank=True, null=True)
    fk_usu_ins = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_usu_ins', blank=True, null=True)
    fk_cur_ins = models.ForeignKey(Curso, models.DO_NOTHING, db_column='fk_cur_ins', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscripcion'


class Profesor(models.Model):
    id_prof = models.AutoField(primary_key=True)
    titulo_prof = models.CharField(max_length=30, blank=True, null=True)
    edad_prof = models.IntegerField(blank=True, null=True)
    pais_prof = models.CharField(max_length=30, blank=True, null=True)
    telefono_prof = models.CharField(max_length=30, blank=True, null=True)
    fk_id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'


class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True)
    nombres_usu = models.CharField(max_length=100, blank=True, null=True)
    apellidos_usu = models.CharField(max_length=100, blank=True, null=True)
    nombre_usuario_usu = models.CharField(max_length=100, blank=True, null=True)
    email_usu = models.CharField(max_length=100, blank=True, null=True)
    password_usu = models.CharField(max_length=100, blank=True, null=True)
    tipo_usu = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
