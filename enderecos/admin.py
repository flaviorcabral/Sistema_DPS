# coding: utf-8
from django import forms
from django.contrib import admin
from .models import *
from.models import Endereco

class EnderecoForm(forms.ModelForm):
 class Media:
  css = {
   'all': ('admin/css/geoposition_override.css',)
  }
  js = ('admin/js/geoposition_override.js',)

class EnderecoAdmin(admin.ModelAdmin):
        form = EnderecoForm       
        model = Endereco
        list_display = ['rua', 'cidade', 'estado', 'bairro']
        search_fields = ['rua', 'cidade']
        list_filter = ['estado',]

admin.site.register(Endereco, EnderecoAdmin)
