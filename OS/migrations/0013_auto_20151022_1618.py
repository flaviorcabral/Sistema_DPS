# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0012_auto_20151022_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordem_servicos',
            name='id',
        ),
        migrations.AddField(
            model_name='ordem_servicos',
            name='numero',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
