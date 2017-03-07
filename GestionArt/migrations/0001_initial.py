# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('fecha_de_Nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=250)),
                ('celular', models.IntegerField(max_length=9)),
                ('direccion', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=75)),
                ('sexo', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tipo', models.CharField(max_length=250)),
                ('matricula', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=250)),
                ('modelo', models.CharField(max_length=250)),
                ('fecha_fabricacion', models.DateField()),
                ('kilometraje', models.IntegerField(max_length=100)),
                ('aclaraciones', models.CharField(max_length=250)),
                ('Client', models.ForeignKey(to='GestionArt.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
