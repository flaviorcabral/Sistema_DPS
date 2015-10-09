# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=20)),
                ('quant', models.PositiveIntegerField()),
                ('valor', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('servico', models.ForeignKey(to='servicos.Servico')),
            ],
        ),
    ]
