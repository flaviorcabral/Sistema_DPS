from django.db import models


# Create your models here.

class InfoAbst(models.Model):
        nome = models.CharField(max_length = 100)
        telefone = models.CharField(max_length=14)
	email = models.EmailField(max_length = 70)

class Meta:
	abstract = True

class Cliente(InfoAbst):
       cpf = models.PositiveIntegerField(blank = True, null = True)
       cnpj = models.PositiveIntegerField(blank = True, null = True)
       endereco = models.ManyToManyField('enderecos.Endereco')
	
       def __unicode__(self):
         return self.nome


