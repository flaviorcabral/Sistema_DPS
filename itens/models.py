from django.db import models

# Create your models here.

class Itens(models.Model):
	nome = models.CharField(max_length = 20)
	descricao = models.CharField(max_length = 50)
	valor = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
	
	def __unicode__(self):
         return self.nome
