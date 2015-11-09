# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_cliente_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='infoabst',
            name='telefone',
            field=models.CharField(help_text=b'Seguir o formato como exemplo: 83-11111-2222', max_length=14),
        ),
    ]
