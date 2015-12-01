# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0005_auto_20151030_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='matricula',
            field=models.CharField(help_text=b'Digitar apenas numeros', unique=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='infoabst',
            name='cpf',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', unique=True, max_length=11),
        ),
    ]
