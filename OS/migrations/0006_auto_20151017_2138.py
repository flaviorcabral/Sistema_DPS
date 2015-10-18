# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_servico_setor'),
        ('OS', '0005_remove_os_setor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='servico',
        ),
        migrations.AddField(
            model_name='os',
            name='servico',
            field=models.ManyToManyField(to='servicos.Servico'),
        ),
    ]
