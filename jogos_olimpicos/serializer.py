from rest_framework import serializers
from jogos_olimpicos.models import Atleta, Evento

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    atleta = AtletaSerializer()
    class Meta:
        model = Evento
        fields = '__all__'