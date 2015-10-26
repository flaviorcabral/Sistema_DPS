# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0018_auto_20151022_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem_servicos',
            name='Observacoes',
            field=models.TextField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
