# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0011_auto_20151018_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servicos',
            name='dataSaida',
            field=models.DateField(blank=True),
        ),
    ]
