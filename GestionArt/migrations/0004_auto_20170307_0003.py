# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionArt', '0003_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='fecha_de_Nacimiento',
            new_name='fecha_de_nacimiento',
        ),
    ]
