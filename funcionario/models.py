from django.db import models

# Create your models here.

class InfoAbst(models.Model):
	nome = models.CharField(max_length = 100)
	telefone = models.PositiveIntegerField()
	cpf = models.PositiveIntegerField()

class Meta:
	abstract = True

class Funcionario(InfoAbst):
	matricula = models.PositiveIntegerField()
	salario = models.DecimalField(max_digits=7, decimal_places=2, default=0) 
	funcao = models.CharField(max_length = 20)
	setor = models.ForeignKey('setor.Setor')
	endereco = models.ManyToManyField('enderecos.Endereco')
