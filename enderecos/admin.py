from django.contrib import admin
from .models import Endereco      

# Register your models here.

class EnderecoAdmin(admin.ModelAdmin):
        model = Endereco      
        list_display = ['rua', 'cep']
        list_filter = ['cep']
        save_on_top = True

admin.site.register(Endereco, EnderecoAdmin)


