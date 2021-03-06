# Generated by Django 3.0.8 on 2020-07-26 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'ordering': ['nombres'],
            },
        ),
        migrations.CreateModel(
            name='DeporteFemenino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='DeporteMasculino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('nombre_corto', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
                'ordering': ['nombre_corto'],
            },
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Alumno')),
                ('femenino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.DeporteFemenino')),
                ('masculino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.DeporteMasculino')),
            ],
            options={
                'ordering': ['alumno'],
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('nombre_corto', models.CharField(max_length=20)),
                ('anho', models.CharField(choices=[('1', '1er Año'), ('2', '2do Año'), ('3', '3er Año'), ('4', '4to Año'), ('5', '5to Año'), ('6', '6to Año'), ('7', '7mo Año'), ('8', '8vo Año')], max_length=1)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Facultad')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'ordering': ['facultad'],
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Carrera'),
        ),
    ]
