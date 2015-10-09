from django.db import models

# Create your models here.

class Itens(models.Model):
	descricao = models.CharField(max_length = 20)
	quant = models.PositiveIntegerField()
	valor = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
	servico = models.ForeignKey('servicos.Servico')
