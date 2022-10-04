from django.contrib import admin
from .models import Prueba, Preguntas, Curso, Estudiante, EstudiantePreguntas, Tema, EstudiantePruebas

admin.site.register(Prueba),
admin.site.register(Preguntas),
admin.site.register(Curso),
admin.site.register(Estudiante),
admin.site.register(EstudiantePreguntas),
admin.site.register(Tema),
admin.site.register(EstudiantePruebas),