# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0003_remove_setor_servico'),
        ('servicos', '0004_remove_servico_setor'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='setor',
            field=models.ForeignKey(default=0, to='setor.Setor'),
            preserve_default=False,
        ),
    ]
