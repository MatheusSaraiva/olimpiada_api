from rest_framework import viewsets, filters
from jogos_olimpicos.models import Atleta, Evento
from jogos_olimpicos.serializer import AtletaSerializer, EventoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AtletasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['sex', 'team', 'noc','sport']
    ordering_fields = ['name',]

class EventoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os atletas nos eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['medal', ]
    search_fields = ['games', 'city', 'event']

