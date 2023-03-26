from .serializers import MemberSerializer,EducaationLevelSerializer,HealthStatusSerializer,BeneficiaryTypeSerializer,HouseholdSerializer,HouseholdProgramSerializer,MaritialStatusSerializer
from registration.models import Member,EducationLevel,HealthStatus,BeneficiaryType,Household,HouseholdProgram,MaritialStatus
from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class=MemberSerializer

class EducationLevelViewSet(viewsets.ModelViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class=EducaationLevelSerializer

class HealthStatusViewSet(viewsets.ModelViewSet):
    queryset = HealthStatus.objects.all()
    serializer_class=HealthStatusSerializer
class BeneficiaryTypeViewSet(viewsets.ModelViewSet):
    queryset = BeneficiaryType.objects.all()
    serializer_class=BeneficiaryTypeSerializer
class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class=HouseholdSerializer
class HouseholdProgramViewSet(viewsets.ModelViewSet):
    queryset = HouseholdProgram.objects.all()
    serializer_class=HouseholdProgramSerializer
class MaritialStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritialStatus.objects.all()
    serializer_class=MaritialStatusSerializer

