from django.db import models
from auditlog.registry import auditlog
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

	SETOR_CHOICES = (

                ('H', 'Software'),
                ('S', 'Hardware'),
        )

	numero = models.AutoField(primary_key=True)
	dataEnt = models.DateField()
	dataSaida = models.DateField(blank = True, null = True)
	status = models.CharField(max_length = 1, choices = STATUS_CHOICES, verbose_name = 'Status')
	pago = models.CharField(max_length = 1, choices = PAGO_CHOICES, verbose_name = 'Pago') 
	formPag = models.CharField(max_length = 1, choices = FORMA_PAG_CHOICES, verbose_name = 'Forma Pagamento', blank = True, null = True)
	setor = models.CharField(max_length = 1, choices = SETOR_CHOICES, verbose_name = 'Setor', blank = True, null = True) 
	servico = models.ManyToManyField('servicos.Servico')
	item = models.ManyToManyField('itens.Itens', blank = True)
        cliente = models.ForeignKey('clientes.Cliente')
        Observacoes = models.TextField(max_length = 100, blank = True, null = True) 
 

auditlog.register(Ordem_Servicos)
