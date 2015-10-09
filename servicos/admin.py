from django.contrib import admin
from servicos.models import Servico      

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
        model = Servico      
        list_display = ['descricao', 'valor']
        list_filter = ['descricao']
        save_on_top = True

admin.site.register(Servico, ServicoAdmin)


