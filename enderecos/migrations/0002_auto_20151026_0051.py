# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ('rua',), 'verbose_name': 'Sua Classe', 'verbose_name_plural': 'Suas Classes'},
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='numero',
        ),
        migrations.AddField(
            model_name='endereco',
            name='position',
            field=geoposition.fields.GeopositionField(default=0, help_text=b'Nao altere os valores calculados automaticamente de latitude e longitude', max_length=42, verbose_name='Geolocalizacao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(help_text=b'Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Belo Horizonte', max_length=255),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='rua',
            field=models.CharField(help_text=b'Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Rua Martinho Estrela,  1229', max_length=255, verbose_name='Endereco'),
        ),
    ]
