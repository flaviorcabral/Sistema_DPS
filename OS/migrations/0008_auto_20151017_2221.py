# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0007_auto_20151017_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='os',
            name='item',
            field=models.ManyToManyField(to='itens.Itens', blank=True),
        ),
    ]
