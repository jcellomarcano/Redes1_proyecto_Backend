from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=120)
	apellido = models.CharField(max_length=120)
	cedula = models.IntegerField()
	telefono = models.IntegerField()
	telefono_emergencia = models.IntegerField()

class Solicitud(models.Model):

	STATUS_CHOICES = (
		("Enviado", "Enviado"),
		("Recibido", "Recibido"),
		("Atendido", "Atendido"),
		("Completa", "Completa"),
	)

	fecha = models.DateField()
	hora = models.TimeField()
	estado = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Enviado")

class Reporte(models.Model):

	STATUS_CHOICES = (
		("Activo", "Activo"),
		("Inactivo", "Inactivo"),
	)

	fecha = models.DateField()
	hora = models.TimeField()
	estado = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Activo")