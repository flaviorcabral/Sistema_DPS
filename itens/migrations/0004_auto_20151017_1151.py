# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0003_remove_itens_quant'),
    ]

    operations = [
        migrations.AddField(
            model_name='itens',
            name='nome',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itens',
            name='descricao',
            field=models.CharField(max_length=50),
        ),
    ]
