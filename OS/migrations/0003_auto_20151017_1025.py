# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_remove_servico_item'),
        ('itens', '0002_remove_itens_servico'),
        ('OS', '0002_auto_20151015_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='os',
            name='item',
            field=models.ForeignKey(default=0, to='itens.Itens'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='os',
            name='servico',
        ),
        migrations.AddField(
            model_name='os',
            name='servico',
            field=models.ForeignKey(default=0, to='servicos.Servico'),
            preserve_default=False,
        ),
    ]
