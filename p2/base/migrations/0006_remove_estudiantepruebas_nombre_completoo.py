# Generated by Django 4.1 on 2022-10-04 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_estudiantepruebas_nombre_completoo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantepruebas',
            name='nombre_completoo',
        ),
    ]
