from django.db import models

# Create your models here.

class Ordem_Servicos(models.Model):
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

	STATUS_SETOR = (

                ('H', 'Hardware'),
                ('S', 'Software'),
        )


	dataEnt = models.DateField()
	dataSaida = models.DateField()
	status = models.CharField(max_length = 1, choices = STATUS_CHOICES, verbose_name = 'Status')
	pago = models.CharField(max_length = 1, choices = PAGO_CHOICES, verbose_name = 'Pago') 
	formPag = models.CharField(max_length = 1, choices = FORMA_PAG_CHOICES, verbose_name = 'Forma Pagamento')
	setor = models.CharField(max_length = 1, choices = STATUS_SETOR, verbose_name = 'Setor') 
	servico = models.ManyToManyField('servicos.Servico')
	item = models.ManyToManyField('itens.Itens', blank = True)
        cliente = models.ForeignKey('clientes.Cliente')
