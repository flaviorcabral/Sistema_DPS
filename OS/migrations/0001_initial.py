# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
        ('setor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataEnt', models.DateField()),
                ('dataSaida', models.DateField()),
                ('status', models.CharField(max_length=1, verbose_name=b'Status', choices=[(b'A', b'Aberta'), (b'F', b'Fechada'), (b'P', b'Pendente')])),
                ('pago', models.CharField(max_length=1, verbose_name=b'Pago', choices=[(b'S', b'Sim'), (b'N', b'Nao')])),
                ('Forma Pagamento', models.CharField(max_length=1, choices=[(b'E', b'Especie'), (b'D', b'Debito'), (b'C', b'Credito')])),
                ('servico', models.ManyToManyField(to='servicos.Servico')),
                ('setor', models.ManyToManyField(to='setor.Setor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
