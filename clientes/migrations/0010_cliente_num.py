# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20151018_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='num',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
