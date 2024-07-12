from django.contrib import admin
from .models import Turno

# Register your models here.

class TurnoAdmin(admin.ModelAdmin):
   # readonly_fields = ('created','updated')
   list_display = ('nombre', 'dni','fecha')
   search_fields =('nombre','dni')

admin.site.register(Turno,TurnoAdmin)


