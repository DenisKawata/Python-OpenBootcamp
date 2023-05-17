# Generated by Django 4.1 on 2023-02-13 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorPelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre Director', max_length=32)),
                ('apellido', models.CharField(help_text='Apellidos Director', max_length=32)),
                ('fechaNacimiento', models.DateField(help_text='Fecha nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre Pelicula', max_length=32)),
                ('descripcion', models.TextField(help_text='Descripcion pelicula', max_length=100)),
                ('duracion', models.PositiveIntegerField(help_text='Duracion en min')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directores.directorpelicula')),
            ],
        ),
    ]