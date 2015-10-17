# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
        ('OS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='setor',
        ),
        migrations.AddField(
            model_name='os',
            name='setor',
            field=models.ForeignKey(default=0, to='setor.Setor'),
            preserve_default=False,
        ),
    ]
