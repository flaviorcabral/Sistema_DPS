from django.contrib import admin
from servicos.models import Servico      

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
        model = Servico      
        list_display = ['descricao', 'setor', 'valor']
        search_fields = ['descricao', 'valor']
	list_filter = ['descricao',]

admin.site.register(Servico, ServicoAdmin)


