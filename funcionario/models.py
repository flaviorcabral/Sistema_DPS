from django.db import models
from auditlog.registry import auditlog
# Create your models here.

class InfoAbst(models.Model):
	nome = models.CharField(max_length = 100)
	telefone = models.CharField(max_length = 15, help_text='Seguir o formato como exemplo: (83)11111-2222')
	cpf = models.PositiveIntegerField(max_length = 11, help_text='Digitar apenas numeros', unique = True)

class Meta:
	abstract = True

class Funcionario(InfoAbst):
	matricula = models.CharField(max_length = 5, help_text='Digitar apenas numeros', unique = True)
	salario = models.DecimalField(max_digits=7, decimal_places=2, default=0) 
	funcao = models.CharField(max_length = 60)
	setor = models.ForeignKey('setor.Setor')
	endereco = models.ManyToManyField('enderecos.Endereco')

	def __unicode__(self):
         return self.nome

auditlog.register(Funcionario)
