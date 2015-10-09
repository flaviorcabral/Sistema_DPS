from django.db import models

# Create your models here.

class OS(models.Model):
	PAGO_CHOICES = (

                ('S', 'Sim'),
                ('N', 'Nao'),
	)

	FORMA_PAG_CHOICES = (

                ('E', 'Especie'),
                ('D', 'Debito'),
		('C', 'Credito'),
        )

	STATUS_CHOICES = (

                ('A', 'Aberta'),
                ('F', 'Fechada'),
                ('P', 'Pendente'),
        )

	dataEnt = models.DateField()
	dataSaida = models.DateField()
	status = models.CharField(max_length = 1, choices = STATUS_CHOICES, verbose_name = 'Status')
	pago = models.CharField(max_length = 1, choices = PAGO_CHOICES, verbose_name = 'Pago') 
	formPag = models.CharField(max_length = 1, choices = FORMA_PAG_CHOICES, name = 'Forma Pagamento')
	servico = models.ManyToManyField('servicos.Servico')
	setor = models.ManyToManyField('setor.Setor')	
        
