# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0004_auto_20151017_1151'),
        ('OS', '0006_auto_20151017_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='item',
        ),
        migrations.AddField(
            model_name='os',
            name='item',
            field=models.ManyToManyField(to='itens.Itens'),
        ),
    ]
