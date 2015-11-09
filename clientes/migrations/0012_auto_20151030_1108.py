# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20151028_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', unique=True, null=True, blank=True),
        ),
    ]
