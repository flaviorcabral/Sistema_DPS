from django.contrib import admin
from setor.models import Setor      

# Register your models here.

class SetorAdmin(admin.ModelAdmin):
        model = Setor      
        list_display = ['nome', 'descricao']
	list_filter = ['nome']
        search_fields = ['nome']
	

admin.site.register(Setor, SetorAdmin)


