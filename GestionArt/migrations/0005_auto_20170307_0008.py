# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionArt', '0004_auto_20170307_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='celular',
            field=models.CharField(max_length=15),
        ),
    ]
