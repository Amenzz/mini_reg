from registration.api.viewsets import FamilyViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Family',FamilyViewSet )