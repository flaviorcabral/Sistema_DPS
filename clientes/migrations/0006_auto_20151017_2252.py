# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20151017_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='infoabst',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
    ]
