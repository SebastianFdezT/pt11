# Generated by Django 4.1 on 2022-10-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_prueba_pruebareal_alter_prueba_calificacionprueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantepruebas',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=40, verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='pruebareal',
            field=models.IntegerField(default=0, verbose_name='Numero de prueba'),
        ),
    ]