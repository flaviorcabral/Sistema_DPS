# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0003_auto_20151026_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ('rua',), 'verbose_name': 'Sua Classe', 'verbose_name_plural': 'Enderecos'},
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(help_text=b'Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Joao Pessoa', max_length=255),
        ),
    ]
