# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.PositiveIntegerField()),
                ('bairro', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=12)),
                ('cidade', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
