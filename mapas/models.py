from django.db import models
from auditlog.registry import auditlog
from geoposition.fields import GeopositionField
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Mapas(models.Model):

        cidade  = models.CharField(max_length=255,help_text="Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Belo Horizonte")
        estado = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
        position = GeopositionField(verbose_name=u'Geolocalizacao', help_text="Nao altere os valores calculados automaticamente de latitude e longitude")

        class Meta:
         verbose_name, verbose_name_plural = u"Sua Classe" , u"Mapas cidades"
         ordering = ('cidade',)

        def __unicode__(self):
         return self.cidade

auditlog.register(Mapas)

