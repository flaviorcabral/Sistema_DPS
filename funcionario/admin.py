from django.contrib import admin
from funcionario.models import InfoAbst
from funcionario.models import Meta
from funcionario.models import Funcionario      

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
        model = Funcionario      
        list_display = ['nome', 'matricula']
	search_fields = ['nome','matricul', 'funcao']
	filter_horizontal = ('endereco',)
	list_filter = ['nome',]

admin.site.register(Funcionario, FuncionarioAdmin)


