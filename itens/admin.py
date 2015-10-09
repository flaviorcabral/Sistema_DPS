from django.contrib import admin
from itens.models import Itens      

# Register your models here.

class ItensAdmin(admin.ModelAdmin):
        model = Itens      
        list_display = ['descricao', 'valor']
        list_filter = ['descricao']
        save_on_top = True

admin.site.register(Itens, ItensAdmin)


