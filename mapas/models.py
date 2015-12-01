from django.db import models
from auditlog.registry import auditlog
from geoposition.fields import GeopositionField
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Mapas(models.Model):

        mapas  = models.CharField(max_length=255)
#        estado = models.CharField(max_length=2, null=True, blank=True)#choices=STATE_CHOICES
        position = GeopositionField(verbose_name=u'Geolocalizacao')

        class Meta:
         verbose_name, verbose_name_plural = u"Sua Classe" , u"GPS"
 #        ordering = ('cidade',)

        def __unicode__(self):
         return self.mapas

auditlog.register(Mapas)

