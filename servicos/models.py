from django.db import models

# Create your models here.

class Servico(models.Model):
	descricao = models.CharField(max_length = 30)
	valor = models.DecimalField(max_digits = 8, decimal_places = 2)
	setor = models.ForeignKey('setor.Setor')
