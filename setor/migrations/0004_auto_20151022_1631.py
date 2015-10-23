# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0003_remove_setor_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='nome',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setor',
            name='descricao',
            field=models.CharField(max_length=50),
        ),
    ]
