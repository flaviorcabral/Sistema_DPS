from django.contrib import admin
from OS.models import Ordem_Servicos      

# Register your models here.

class OsAdmin(admin.ModelAdmin):
        model = Ordem_Servicos      
        list_display = ['numero','status', 'cliente', 'setor']
	search_fields = ['numero']
       	list_filter = ['status', 'cliente', 'setor']
	filter_horizontal =  ('servico', 'item',)
	list_filter = ['cliente',] 
	ordering = ('-dataEnt',)
	date_hierarchy = 'dataEnt'


admin.site.register(Ordem_Servicos, OsAdmin)

# Register your models here.
