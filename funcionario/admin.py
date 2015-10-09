from django.contrib import admin
from funcionario.models import InfoAbst
from funcionario.models import Meta
from funcionario.models import Funcionario      

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
        model = Funcionario      
        list_display = ['nome', 'matricula']
        list_filter = ['nome']
        save_on_top = True

admin.site.register(Funcionario, FuncionarioAdmin)


