from django.contrib import admin
from setor.models import Setor      

# Register your models here.

class SetorAdmin(admin.ModelAdmin):
        model = Setor      
        list_display = ['descricao']
#       list_filter = ['descricao']
        search_fields = ['descricao']


admin.site.register(Setor, SetorAdmin)


