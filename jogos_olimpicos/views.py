from rest_framework import viewsets
from rest_framework.response import Response

from jogos_olimpicos.models import Atleta, Evento
from jogos_olimpicos.serializer import AtletaSerializer, EventoSerializer


class AtletasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os atletas nos eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


