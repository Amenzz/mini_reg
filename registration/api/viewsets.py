from registration.models import Family
from .serializers import FamilySerializer
from rest_framework import viewsets

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class=FamilySerializer