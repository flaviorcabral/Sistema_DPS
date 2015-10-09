# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=30)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('setor', models.ForeignKey(to='setor.Setor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
