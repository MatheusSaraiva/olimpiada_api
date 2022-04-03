from rest_framework import viewsets, filters

from jogos_olimpicos.models import Atleta, Evento, NOC_team
from jogos_olimpicos.serializer import AtletaSerializer, EventoSerializer, NOC_team_Serializer
from django_filters.rest_framework import DjangoFilterBackend


class NOC_team_ViemSet(viewsets.ModelViewSet):
    queryset = NOC_team.objects.all()
    serializer_class = NOC_team_Serializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['noc', 'team']
    filterset_fields = ['noc','team']
    ordering_fields = ['team',]


class AtletasViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['sex','sport']
    ordering_fields = ['name',]


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['medal', ]
    search_fields = ['games', 'city', 'event']



