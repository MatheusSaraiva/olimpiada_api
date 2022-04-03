from django.contrib import admin
from django.urls import path, include
from jogos_olimpicos.views import AtletasViewSet, EventoViewSet, NOC_team_ViemSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Olimpiada API",
      default_version='v1',
      description="Uma API rest para servir os dados do dataset"
                  " “120 years of Olympic history: athletes and results” presente no Kaggle",
      terms_of_service="#",
      contact=openapi.Contact(email="saraivarego@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('atletas', AtletasViewSet, basename='Atletas')
router.register('atletas_eventos', EventoViewSet, basename='Atletas_Eventos')
router.register('NOC_team', NOC_team_ViemSet, basename='NOC_team')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
