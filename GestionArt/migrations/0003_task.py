# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionArt', '0002_client_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('icono', models.CharField(max_length=1000)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_comienzo', models.DateTimeField()),
                ('fecha_finalizacion', models.DateTimeField()),
                ('responsable', models.CharField(max_length=250)),
                ('Vehicle', models.ForeignKey(to='GestionArt.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
