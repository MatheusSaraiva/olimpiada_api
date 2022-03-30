from django.contrib import admin
from django.urls import path, include
from jogos_olimpicos.views import AtletasViewSet, EventoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('atletas', AtletasViewSet, basename='Atletas')
router.register('atletas_eventos', EventoViewSet, basename='Atletas_Eventos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
