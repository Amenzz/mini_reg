from rest_framework import serializers
from registration.models import Member,EducationLevel,HealthStatus,BeneficiaryType,Household,HouseholdProgram,MaritialStatus

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=(
            '__all__'
        )
class EducaationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=EducationLevel
        fields=(
            'EducationLevel',
        )
class HealthStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=HealthStatus
        fields=(
            'HealthStatus',
        )

class BeneficiaryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BeneficiaryType
        fields=(
            'BeneficiaryType',
        )
class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Household
        fields=(
            '__all__'
        )
class HouseholdProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model=HouseholdProgram
        fields=(
            'HouseholdProgram',
        )
class MaritialStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaritialStatus
        fields=(
            'MaritialStatus',
        )