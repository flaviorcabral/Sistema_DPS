# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_auto_20151022_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='matricula',
            field=models.CharField(help_text=b'Digitar apenas numeros', max_length=20),
        ),
        migrations.AlterField(
            model_name='infoabst',
            name='cpf',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros'),
        ),
        migrations.AlterField(
            model_name='infoabst',
            name='telefone',
            field=models.PositiveIntegerField(help_text=b'Seguir o formato como exemplo: 83-11111-2222'),
        ),
    ]
