# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151017_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='os',
            field=models.ForeignKey(to='OS.OS', null=True),
        ),
    ]
