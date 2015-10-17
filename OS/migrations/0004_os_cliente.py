# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_remove_cliente_os'),
        ('OS', '0003_auto_20151017_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='os',
            name='cliente',
            field=models.ForeignKey(default=0, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
