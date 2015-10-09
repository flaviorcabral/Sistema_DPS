# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0001_initial'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAbst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('infoabst_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='clientes.InfoAbst')),
                ('cpf', models.PositiveIntegerField()),
                ('endereco', models.ManyToManyField(to='enderecos.Endereco')),
                ('os', models.ForeignKey(to='OS.OS')),
            ],
            options={
            },
            bases=('clientes.infoabst',),
        ),
    ]
