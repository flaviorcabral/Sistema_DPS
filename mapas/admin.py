
# coding: utf-8
from django import forms
from django.contrib import admin
from .models import *
from.models import Mapas

class MapasForm(forms.ModelForm):
 class Media:
  css = {
   'all': ('admin/css/geoposition_override.css',)
  }
  js = ('admin/js/geoposition_override.js',)

class MapasAdmin(admin.ModelAdmin):
        form = MapasForm
        model = Mapas
        list_display = ['mapas']
#        search_fields = ['cidade']
#        list_filter = ['estado',]
        readonly_fields = ('mapas',)
 
admin.site.register(Mapas, MapasAdmin)

