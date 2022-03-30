from rest_framework import viewsets
from jogos_olimpicos.models import Atleta, Evento
from jogos_olimpicos.serializer import AtletaSerializer


class AtletasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


