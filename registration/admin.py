from django.contrib import admin
from .models import Household,Member,EducationLevel,HealthStatus,MaritialStatus,BeneficiaryType,HouseholdProgram
# Register your models here.
admin.site.register(Household)
admin.site.register(Member)
admin.site.register(EducationLevel)
admin.site.register(HealthStatus)
admin.site.register(MaritialStatus)
admin.site.register(BeneficiaryType)
admin.site.register(HouseholdProgram)