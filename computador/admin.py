from django.contrib import admin
from .models import Computador, pecasDeComputador


class ComputadorAdmin(admin.ModelAdmin):
    list_display = ('nome'),
    search_fields = ('nome'),
    
class pecasDeComputadorAdmin(admin.ModelAdmin):
    list_display = ('processador', 'memoriaRam', 'placaMae', 'armazenamento', 'placaDeVideo', 'fonte')
    search_fields = ('processador', 'memoriaRam', 'placaMae', 'armazenamento', 'placaDeVideo', 'fonte')
    list_filter = ['processador']


admin.site.register(Computador, ComputadorAdmin)
admin.site.register(pecasDeComputador, pecasDeComputadorAdmin)

