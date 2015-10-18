from django.db import models

# Create your models here.

class Endereco(models.Model):

	rua = models.CharField(max_length = 50)
	numero = models.PositiveIntegerField()
	bairro = models.CharField(max_length = 20)
	cep = models.CharField(max_length = 12)
	cidade  = models.CharField(max_length = 15)
	estado = models.CharField(max_length = 15)	

	def __unicode__(self):
         return self.rua
 	 
