from django.db import models
from datetime import date
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType




# Create your models here.


#Below here is Beneficiary Type model
class BeneficiaryType(models.Model):
     Beneficiary_Choice=(
        ('Primary','Primary_Beneficiary'),
        ('Contingent', 'Contingent_Benficiary'),
    )
     BeneficiaryType=models.CharField(max_length=100,choices=Beneficiary_Choice)
#Below here is EducationLevel model
class EducationLevel(models.Model):
     Education_Status=(
        ('Elementaty','Elementary'),
        ('HighSchool','HighSchool'),
        ('Undergraduate','Undergraduate'),
        ('Postgraduate','Postgraduate'),
    )     
     EducationLevel=models.CharField(max_length=100,choices=Education_Status,null=True)
#Below here is HealthStatus model
class HealthStatus(models.Model):
     Health_status=(
        ('Healthy','Healthy'),
        ('UnHealthy','UnHealthy'),
    )
     HealthStatus=models.CharField(max_length=100,choices=Health_status,null=True)
#Below here is Marriage Status
class MaritialStatus(models.Model):
     Maritial_Status=(
        ('single','single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
        ('Widowed','Widowed'),

    )
        
     MaritialStatus=models.CharField(max_length=100,choices=Maritial_Status,null=True)
#Below here is Househodl Program Model

class HouseholdProgram(models.Model):
     Household_program=(
        ('Childcare','Childcare'),
        ('disabled','Disabled'),
        ('Dependent','Dependent'),
        ('cleaning','Cleaning'),
        ('Meal preparation','Meal Preparation'),
    )
     HouseholdProgram=models.CharField(max_length=100,choices=Household_program,null=True)

#Belo out here is Household Mddel



class Household(models.Model):
   
    CreatedDate=models.DateTimeField(auto_now_add=True,null=True)
    updatedDate=models.DateTimeField(auto_now=True,null=True)
    
    Active=1
    Inactive=0
    Status_choice=((Active,'Active'),(Inactive,'Inactive'))
    Status=models.IntegerField(choices=Status_choice,default=Active,null=True)
    HouseHoldIdNumber=models.CharField(max_length=40)
    MaleMemberSize=models.IntegerField(null=True)
    FemaleMemberSize=models.IntegerField(null=True)
    NumberOfParticipatingMale=models.IntegerField(null=True)
    NumberOfParticipatingFemale=models.IntegerField(null=True)
    NumberOfMaleBody=models.IntegerField(null=True)
    NumberOfFemaleBody=models.IntegerField(null=True)
    RegistrationDate=models.DateField(null=True)
    HouseHoldProgram=models.ForeignKey(HouseholdProgram, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
         return f"{self.id} "
    @property
    def CreatedBy(self):
        CreatedBy= self.pk
        return CreatedBy
    @property
    def UpdatedBy(self):
        UpdatedBy= self.pk
        return UpdatedBy
#below out here is Member Model

class Member(models.Model):
     CreatedDate=models.DateTimeField(auto_now_add=True,null=True)
     updatedDate=models.DateTimeField(auto_now=True,null=True)
     Active=1
     Inactive=0
     Status_choice=((Active,'Active'),(Inactive,'Inactive'))
     Status=models.IntegerField(choices=Status_choice,default=Active,null=True)
     Household=models.ForeignKey(Household,on_delete=models.CASCADE, null=True, blank=True)
     HouseholdMemberIdNumber=models.CharField(max_length=40)
     NationalMemberIdNumber=models.CharField(max_length=40)
     FirstName=models.CharField(max_length=40)
     FatherName=models.CharField(max_length=40)
     GrandFatherName=models.CharField(max_length=40)
     MotherFullName=models.CharField(max_length=40)
     Gender_Choice=(
        ('M','Male'),
        ('F','Female'),
     )
     Gender=models.CharField(max_length=1,choices=Gender_Choice)
     DateOfBirth=models.DateField(null=True, blank =True)
     age=models.IntegerField(null=True, blank=True)
    
     @property
     def age(self):
          age=date.today().year=self.DateOfBirth.year
          return age
     BeneficiaryType=models.ForeignKey(BeneficiaryType,on_delete=models.CASCADE,null=True,blank=True)
     #RelationToHousehold=models.ForeignKey(Household,on_delete=models.CASCADE,null=True,blank=True)
     RegistrationDate=models.DateField(null=True,blank=True)
     EducationLevel=models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True, blank=True)
     HealthStatus=models.ForeignKey(HealthStatus, on_delete=models.CASCADE, null=True,blank=True)
     MaritialStatus=models.ForeignKey(MaritialStatus, on_delete=models.CASCADE,null=True,blank=True)
     @property
     def CreatedBy(self):
        CreatedBy= self.FirstName
        return CreatedBy
     @property
     def UpdatedBy(self):
        UpdatedBy= self.FirstName
        return UpdatedBy

