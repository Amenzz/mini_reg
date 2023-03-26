from registration.api.viewsets import MemberViewSet,HouseholdViewSet,HealthStatusViewSet,EducationLevelViewSet,BeneficiaryTypeViewSet,HouseholdProgramViewSet,MaritialStatusViewSet
from rest_framework import routers

#Below here is  Model of router 
router=routers.DefaultRouter()
router.register('Member',MemberViewSet ),
router.register('Household',HouseholdViewSet ),
router.register('Health Status',HealthStatusViewSet ),
router.register('Education Level',EducationLevelViewSet ),
router.register('Beneficiary Type',BeneficiaryTypeViewSet ),
router.register('Household Program',HouseholdProgramViewSet ),
router.register('Maritial Status',MaritialStatusViewSet ),