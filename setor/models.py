from django.db import models

# Create your models here.

class Setor(models.Model):

	descricao = models.CharField(max_length = 15)
