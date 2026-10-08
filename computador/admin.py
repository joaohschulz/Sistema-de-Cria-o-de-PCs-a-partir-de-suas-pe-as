from django.contrib import admin
from .models import Computador, pecasDeComputador, Processador, PlacaMae, MemoriaRam, Armazenamento, PlacaDeVideo, Fonte


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
    list_display = ('placaMae', 'socket', 'chipset', 'tipo_memoria')
class MemoriaRamAdmin(admin.ModelAdmin):
    list_display = ('memoriaRam',)
class ArmazenamentoAdmin(admin.ModelAdmin):
    list_display = ('armazenamento',)
class PlacaDeVideoAdmin(admin.ModelAdmin):
    list_display = ('placaDeVideo',)
class FonteAdmin(admin.ModelAdmin):
    list_display = ('fonte',)

admin.site.register(Computador, ComputadorAdmin)
admin.site.register(pecasDeComputador, pecasDeComputadorAdmin)
admin.site.register(Processador, ProcessadorAdmin)
admin.site.register(PlacaMae, PlacaMaeAdmin)
admin.site.register(MemoriaRam, MemoriaRamAdmin)
admin.site.register(Armazenamento, ArmazenamentoAdmin)
admin.site.register(PlacaDeVideo, PlacaDeVideoAdmin)
admin.site.register(Fonte, FonteAdmin)

