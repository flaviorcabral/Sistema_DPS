# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_servico_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='item',
        ),
    ]
