from django.db import models

# Create your models here.

class InfoAbst(models.Model):
        nome = models.CharField(max_length = 100)
        telefone = models.PositiveIntegerField()
	email = models.EmailField(max_length = 70)

class Meta:
	abstract = True

class Cliente(InfoAbst):
        cpf = models.PositiveIntegerField()
        endereco = models.ForeignKey('enderecos.Endereco')
	
	def __unicode__(self):
         return self.nome


