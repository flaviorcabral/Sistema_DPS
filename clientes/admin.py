from django.contrib import admin
from clientes.models import InfoAbst
from clientes.models import Meta
from clientes.models import Cliente
#from clientes.forms import MyModelFormAdmin
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	list_display = ['nome', 'telefone', 'email']
	filter_horizontal = ('endereco',)
	save_on_top = True

#class ModelAdmin(admin.ModelAdmin):
#	form = MyModelFormAdmin

admin.site.register(Cliente, ClienteAdmin)
