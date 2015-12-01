# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20151030_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', max_length=14, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.PositiveIntegerField(help_text=b'Digitar apenas numeros', max_length=11, unique=True, null=True, blank=True),
        ),
    ]
