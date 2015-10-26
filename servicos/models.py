from django.db import models
from auditlog.registry import auditlog
# Create your models here.

class Servico(models.Model):
	descricao = models.CharField(max_length = 30)
	valor = models.DecimalField(max_digits = 8, decimal_places = 2)
	setor = models.ForeignKey('setor.Setor')
	
	def __unicode__(self):
         return self.descricao

auditlog.register(Servico)
