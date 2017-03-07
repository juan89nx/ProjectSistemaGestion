# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionArt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cedula',
            field=models.CharField(max_length=10, default=4247920),
            preserve_default=False,
        ),
    ]
