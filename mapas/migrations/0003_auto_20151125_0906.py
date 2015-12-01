# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapas', '0002_auto_20151110_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapas',
            options={'ordering': ('cidade',), 'verbose_name': 'Sua Classe', 'verbose_name_plural': 'GPS'},
        ),
    ]
