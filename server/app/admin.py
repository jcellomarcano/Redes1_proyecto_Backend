from django.contrib import admin
from app.models import *
from django import forms

"""class UsuarioForm(forms.ModelForm):
	fields = ["nombre","apellido","cedula","telefono","telefono_emergencia"]
	class Meta:
		model = Usuario

class UsuarioAdmin(admin.ModelAdmin):
	form = UsuarioForm"""

admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(Reporte)