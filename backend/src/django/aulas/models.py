from django.db import models

# Create your models here.
from django.db import models


class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return f"carrera: {self.nombre}"
    def __unicode__(self):
        return f"carrera: {self.nombre}"

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def __unicode__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField(default=5)
    id_carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        db_column='id_carrera',
    )
    id_profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        db_column='id_profesor',
    )

    def __str__(self):
        return f"materia: {self.nombre} - cantidad alumnos: {self.cant_alumnos} - carrera: {self.id_carrera.nombre} - profesor: {self.id_profesor.nombre} {self.id_profesor.apellido}"
    
    def __unicode__(self):
        return f"materia: {self.nombre} - cantidad alumnos: {self.cant_alumnos} - carrera: {self.id_carrera.nombre} - profesor: {self.id_profesor.nombre} {self.id_profesor.apellido}   "



class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return f"aula: {self.descripcion} - ubicacion: {self.ubicacion} - cantidad proyectores: {self.cant_proyector} - aforo: {self.aforo} - es climatizada: {self.es_climatizada}"
    def __unicode__(self):
        return f"aula: {self.descripcion} - ubicacion: {self.ubicacion} - cantidad proyectores: {self.cant_proyector} - aforo: {self.aforo} - es climatizada: {self.es_climatizada}"


class ReservaAula(models.Model):
    id = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        db_column='id_aula',
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observaciones = models.CharField(max_length=256)

class HorarioMateria(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        db_column='id_materia',
    )
    id_reserva = models.ForeignKey(
        ReservaAula,
        on_delete=models.CASCADE,
        db_column='id_reserva',
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()