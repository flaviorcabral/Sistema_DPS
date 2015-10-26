from django.db import models
from auditlog.registry import auditlog
# Create your models here.

class Setor(models.Model):
	nome = models.CharField(max_length = 15)
	descricao = models.CharField(max_length = 50)

	def __unicode__(self):
         return self.nome

auditlog.register(Setor)
