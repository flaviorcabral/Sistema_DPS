from django.contrib import admin
from.models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
        model = Endereco
        list_display = ['rua', 'cidade', 'estado', 'bairro']
        list_filter = ['rua']
        save_on_top = True

admin.site.register(Endereco, EnderecoAdmin)
