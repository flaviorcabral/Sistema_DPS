from django.db import models
from auditlog.registry import auditlog
from geoposition.fields import GeopositionField
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Endereco(models.Model):

	rua = models.CharField(max_length=255, verbose_name=u'Endereco', help_text='Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Rua Martinho Estrela,  1229')
	bairro = models.CharField(max_length = 20)
	cep = models.CharField(max_length = 12)
	cidade  = models.CharField(max_length=255,help_text="Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Belo Horizonte")
	estado = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
	position = GeopositionField(verbose_name=u'Geolocalizacao', help_text="Nao altere os valores calculados automaticamente de latitude e longitude")
	
	class Meta:
         verbose_name, verbose_name_plural = u"Sua Classe" , u"Suas Classes"
         ordering = ('rua',)

	def __unicode__(self):
         return self.rua
 	 
auditlog.register(Endereco)
