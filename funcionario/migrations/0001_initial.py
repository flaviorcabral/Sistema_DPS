# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAbst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.PositiveIntegerField()),
                ('cpf', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('infoabst_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='funcionario.InfoAbst')),
                ('matricula', models.PositiveIntegerField()),
                ('salario', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('funcao', models.CharField(max_length=20)),
                ('endereco', models.ManyToManyField(to='enderecos.Endereco')),
                ('setor', models.ForeignKey(to='setor.Setor')),
            ],
            options={
            },
            bases=('funcionario.infoabst',),
        ),
    ]
