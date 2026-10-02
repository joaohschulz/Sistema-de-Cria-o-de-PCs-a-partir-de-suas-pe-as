from django.contrib import admin
from .models import Computador, pecasDeComputador


class ComputadorAdmin(admin.ModelAdmin):
    list_display = ('nome'),
    search_fields = ('nome'),
    
class pecasDeComputadorAdmin(admin.ModelAdmin):
    list_display = ('processador', 'memoriaRam', 'placaMae', 'armazenamento', 'placaDeVideo', 'fonte')
    search_fields = ('processador', 'memoriaRam', 'placaMae', 'armazenamento', 'placaDeVideo', 'fonte')
    list_filter = ['processador']
class ProcessadorAdmin(admin.ModelAdmin):
    list_display = ('processador',)
class PlacaMaeAdmin(admin.ModelAdmin):
    list_display = ('placaMae',)
class MemoriaRam(admin.ModelAdmin):
    list_display = ('memoriaRam',)
class ArmazenamentoAdmin(admin.ModelAdmin):
    list_display = ('armazenamento',)
class PlacaDeVideo(admin.ModelAdmin):
    list_display = ('placaDeVideo',)
class Fonte(admin.ModelAdmin):
    list_display = ('fonte',)

admin.site.register(Computador, ComputadorAdmin)
admin.site.register(pecasDeComputador, pecasDeComputadorAdmin)

