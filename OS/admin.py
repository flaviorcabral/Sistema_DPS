from django.contrib import admin
from OS.models import Ordem_Servicos      

# Register your models here.

class OsAdmin(admin.ModelAdmin):
        model = Ordem_Servicos      
        list_display = ['status', 'cliente', 'setor']
       	filter_horizontal =  ('servico', 'item',)
        save_on_top = True

admin.site.register(Ordem_Servicos, OsAdmin)

# Register your models here.
