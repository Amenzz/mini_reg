from rest_framework import serializers
from registration.models import Family

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model=Family
        fields=('Name','LastName','MotherName','Age','BirthDay')