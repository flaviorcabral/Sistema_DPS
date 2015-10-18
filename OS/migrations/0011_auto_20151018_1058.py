# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20151018_0842'),
        ('itens', '0004_auto_20151017_1151'),
        ('servicos', '0005_servico_setor'),
        ('OS', '0010_auto_20151018_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem_Servicos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataEnt', models.DateField()),
                ('dataSaida', models.DateField()),
                ('status', models.CharField(max_length=1, verbose_name=b'Status', choices=[(b'A', b'Aberta'), (b'F', b'Fechada'), (b'P', b'Pendente')])),
                ('pago', models.CharField(max_length=1, verbose_name=b'Pago', choices=[(b'S', b'Sim'), (b'N', b'Nao')])),
                ('formPag', models.CharField(max_length=1, verbose_name=b'Forma Pagamento', choices=[(b'E', b'Especie'), (b'D', b'Debito'), (b'C', b'Credito')])),
                ('setor', models.CharField(max_length=1, verbose_name=b'Setor', choices=[(b'H', b'Hardware'), (b'S', b'Software')])),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('item', models.ManyToManyField(to='itens.Itens', blank=True)),
                ('servico', models.ManyToManyField(to='servicos.Servico')),
            ],
        ),
        migrations.RemoveField(
            model_name='os',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='os',
            name='item',
        ),
        migrations.RemoveField(
            model_name='os',
            name='servico',
        ),
        migrations.DeleteModel(
            name='OS',
        ),
    ]
