from django.contrib import admin
from jogos_olimpicos.models import Atleta, Evento

class Atletas(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'sport')
    list_display_links = ('id', 'name')
    search_fieldas = ('name',)
    list_per_page = 20

admin.site.register(Atleta, Atletas)

class Eventos(admin.ModelAdmin):
    list_display = ('id', 'event', 'games')
    list_display_links = ('id', 'event')
    search_fieldas = ('event',)
    list_per_page = 20

admin.site.register(Evento, Eventos)