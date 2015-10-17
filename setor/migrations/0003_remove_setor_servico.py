# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0002_setor_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='servico',
        ),
    ]
