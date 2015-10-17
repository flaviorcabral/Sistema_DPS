# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_remove_itens_servico'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='item',
            field=models.ForeignKey(default=1, to='itens.Itens'),
            preserve_default=False,
        ),
    ]
