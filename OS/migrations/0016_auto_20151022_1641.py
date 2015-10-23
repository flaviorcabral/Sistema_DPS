# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0015_auto_20151022_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servicos',
            name='dataSaida',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordem_servicos',
            name='formPag',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Forma Pagamento', choices=[(b'E', b'Especie'), (b'D', b'Debito'), (b'C', b'Credito')]),
        ),
    ]
