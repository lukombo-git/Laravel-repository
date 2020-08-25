from rest_framework.viewsets import ModelViewSet

from .serializers import CandidatesSerializer,VagasSerializer

from .models import Candidates,Vagas

class CandidatesViewSet(ModelViewSet):
    queryset= Candidates.objects.all()
    serializer_class = CandidatesSerializer

class VagasViewSet(ModelViewSet):
    queryset= Vagas.objects.all()
    serializer_class = VagasSerializer
