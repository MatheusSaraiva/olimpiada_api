from rest_framework import serializers, pagination
from jogos_olimpicos.models import Atleta, Evento, NOC_team


class NOC_team_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NOC_team
        fields = '__all__'

class AtletaSerializer(serializers.ModelSerializer):
    noc = serializers.ReadOnlyField(source='noc_team.noc')
    team = serializers.ReadOnlyField(source='noc_team.team')
    class Meta:
        model = Atleta
        fields = ['id', 'name', 'sex', 'sport', 'noc', 'team']

class EventoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='atleta.id')
    name = serializers.ReadOnlyField(source='atleta.name')
    sex = serializers.ReadOnlyField(source='atleta.sex')
    sport = serializers.ReadOnlyField(source='atleta.sport')
    noc = serializers.ReadOnlyField(source='atleta.noc_team.noc')
    team = serializers.ReadOnlyField(source='atleta.noc_team.team')

    class Meta:
        model = Evento
        fields = ['id', 'name','sex','age','height', 'weight', 'team', 'noc', 'games',
                  'year', 'season', 'city', 'sport', 'event', 'medal']



