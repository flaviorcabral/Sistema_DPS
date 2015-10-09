from django.contrib import admin
from OS.models import OS      

# Register your models here.

class OsAdmin(admin.ModelAdmin):
        model = OS      
        list_display = ['status']
        list_filter = ['status']
        save_on_top = True

admin.site.register(OS, OsAdmin)

# Register your models here.
