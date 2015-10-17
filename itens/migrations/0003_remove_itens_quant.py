# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_remove_itens_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itens',
            name='quant',
        ),
    ]
