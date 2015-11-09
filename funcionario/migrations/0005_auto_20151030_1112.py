# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_auto_20151030_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoabst',
            name='telefone',
            field=models.CharField(help_text=b'Seguir o formato como exemplo: (83)11111-2222', max_length=15),
        ),
    ]
