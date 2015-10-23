# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0016_auto_20151022_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servicos',
            name='setor',
            field=models.CharField(max_length=2, verbose_name=b'Setor', choices=[(b'H', b'Hardware'), (b'S', b'Software')]),
        ),
    ]
