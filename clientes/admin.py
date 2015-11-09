from django.contrib import admin
from clientes.models import InfoAbst
from clientes.models import Meta
from clientes.models import Cliente
#from clientes.forms import ClienteForm

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
#	form = ClienteForm
	model = Cliente
	list_display = ['nome','telefone', 'email']
	search_fields = ['nome', 'email']
	filter_horizontal = ('endereco',)
	list_filter = ['nome',]

admin.site.register(Cliente, ClienteAdmin)
