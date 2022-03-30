from django.contrib import admin
from django.urls import path, include
from jogos_olimpicos.views import AtletasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('atletas', AtletasViewSet, basename='Atletas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
