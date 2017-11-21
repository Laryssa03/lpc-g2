from rest_framework import routers, serializers, viewsets
from votacao.models import *
class EleitorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Eleitor
        fields = '__all__'
class EleicaoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Eleicao
        fields = '__all__'
class VagaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vaga
        fields = '__all__'

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Candidato
        fields = '__all__'
class TokenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'
class UrnaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Urna
        fields = '__all__'