from rest_framework import serializers

from .models import Candidates,Vagas


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields ='__all__'
        
class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields ='__all__'
