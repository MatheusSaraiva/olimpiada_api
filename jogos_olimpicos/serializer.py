from rest_framework import serializers
from jogos_olimpicos.models import Atleta, Evento

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'