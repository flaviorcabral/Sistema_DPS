# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_remove_servico_setor'),
        ('setor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='servico',
            field=models.ForeignKey(default=0, to='servicos.Servico'),
            preserve_default=False,
        ),
    ]
