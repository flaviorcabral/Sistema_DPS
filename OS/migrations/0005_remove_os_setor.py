# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0004_os_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='setor',
        ),
    ]
