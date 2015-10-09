from django.contrib import admin
from clientes.models import InfoAbst
from clientes.models import Meta
from clientes.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	list_display = ['nome', 'email']
	list_filter = ['nome']
	save_on_top = True

admin.site.register(Cliente, ClienteAdmin)
