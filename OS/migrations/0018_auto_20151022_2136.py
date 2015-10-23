# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0017_auto_20151022_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servicos',
            name='setor',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Setor', choices=[(b'H', b'Software'), (b'S', b'Hardware')]),
        ),
    ]
