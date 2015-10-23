from django.contrib import admin
from.models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
        model = Endereco
        list_display = ['rua', 'cidade', 'estado', 'bairro']
        search_fields = ['rua', 'cidade', 'estado', 'bairro']


admin.site.register(Endereco, EnderecoAdmin)
