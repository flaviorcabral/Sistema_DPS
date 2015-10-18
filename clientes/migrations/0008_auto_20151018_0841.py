# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20151018_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.PositiveIntegerField(max_length=14, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.PositiveIntegerField(max_length=11, null=True, blank=True),
        ),
    ]
