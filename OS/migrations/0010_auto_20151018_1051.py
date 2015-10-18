# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0009_os_setor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='Forma Pagamento',
        ),
        migrations.AddField(
            model_name='os',
            name='formPag',
            field=models.CharField(default=0, max_length=1, verbose_name=b'Forma Pagamento', choices=[(b'E', b'Especie'), (b'D', b'Debito'), (b'C', b'Credito')]),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='os',
            name='setor',
        ),
        migrations.AddField(
            model_name='os',
            name='setor',
            field=models.CharField(default=0, max_length=1, verbose_name=b'Setor', choices=[(b'H', b'Hardware'), (b'S', b'Software')]),
            preserve_default=False,
        ),
    ]
