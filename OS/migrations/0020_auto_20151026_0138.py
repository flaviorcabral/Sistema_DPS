# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0019_ordem_servicos_observacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servicos',
            name='Observacoes',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
