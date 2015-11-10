from django.db import models
from auditlog.registry import auditlog
from geoposition.fields import GeopositionField
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Endereco(models.Model):

	rua = models.CharField(max_length=255)
	bairro = models.CharField(max_length = 20)
	cep = models.CharField(max_length = 12)
	cidade  = models.CharField(max_length=255)
	estado = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
	
	class Meta:
         verbose_name, verbose_name_plural = u"Sua Classe" , u"Enderecos"
         ordering = ('rua',)

	def __unicode__(self):
         return self.rua
 	 
auditlog.register(Endereco)
