# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0013_auto_20151022_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordem_servicos',
            name='numero',
        ),
        migrations.AddField(
            model_name='ordem_servicos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
