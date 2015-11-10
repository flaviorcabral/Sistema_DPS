# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0004_auto_20151028_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='position',
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='rua',
            field=models.CharField(max_length=255),
        ),
    ]
