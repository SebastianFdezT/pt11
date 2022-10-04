from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Prueba(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pruebas')
    nombre_prueba = models.CharField('Nombre Prueba', max_length=100)
    aciertoprueba = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    calificacionprueba = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    pruebareal = models.IntegerField('Numero de prueba', default=0)

    def __str__(self):
        return str(self.id) + '-' + self.nombre_prueba

class Tema(models.Model):
    nombre_tema = models.CharField('Nombre Tema', max_length=100)

    aciertotema = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return str(self.id) + '-' + self.nombre_tema

class Preguntas(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    pregunta = models.CharField('Pregunta', max_length=100)
    acierto = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
 
    def nombreprueba(self):
        return self.prueba.nombre_prueba

    def nombretema(self):
        return self.tema.nombre_tema

    def __str__(self):
        return str(self.id) + '-' + self.pregunta

class Curso(models.Model):
    nombre_curso = models.CharField('Nombre del Curso', max_length=100)

    def __str__(self):
        return self.nombre_curso        

class Estudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    nombres = models.CharField('Nombres', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    nombre_completo = models.CharField('Nombre Completo', max_length=40, blank=True)
    aciertoestudiante = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)

    preguntas = models.ManyToManyField(Preguntas,through='EstudiantePreguntas', blank=True)

    def save(self):
        self.nombre_completo = self.nombres + ' ' + self.apellidos
        return super(Estudiante, self).save()

    #class Meta:
    #    verbose_name = 'Estudiante'
    #    verbose_name_plural = 'Estudiantes del curso'
    #    ordering = ['-nombres', 'apellidos']

    def cursoestudiante(self):
        return self.curso

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class EstudiantePreguntas(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)

    correcto = models.BooleanField()

    def nombresestudiante(self):
        return  self.estudiante.nombres + ' ' + self.estudiante.apellidos

    def __str__(self):
        return self.estudiante.nombres + ' ' + self.estudiante.apellidos + ' ' + self.preguntas.pregunta + ' ' + str(self.correcto)

class EstudiantePruebas(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    calificacion = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def nombresestudiantee(self):
        return  self.estudiante.nombre_completo

    def __str__(self):
        return str(self.calificacion)