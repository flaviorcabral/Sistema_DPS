# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20151017_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cnpj',
            field=models.PositiveIntegerField(default=0, max_length=14, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.PositiveIntegerField(max_length=11, blank=True),
        ),
    ]
