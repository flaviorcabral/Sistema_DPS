# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0003_remove_setor_servico'),
        ('OS', '0008_auto_20151017_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='os',
            name='setor',
            field=models.ManyToManyField(to='setor.Setor'),
        ),
    ]
