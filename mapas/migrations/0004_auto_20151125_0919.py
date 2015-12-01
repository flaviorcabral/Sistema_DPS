# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapas', '0003_auto_20151125_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapas',
            options={'verbose_name': 'Sua Classe', 'verbose_name_plural': 'GPS'},
        ),
        migrations.RenameField(
            model_name='mapas',
            old_name='cidade',
            new_name='mapas',
        ),
        migrations.RemoveField(
            model_name='mapas',
            name='estado',
        ),
    ]
