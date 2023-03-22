from django.db import models

# Create your models here.

class Household(models.Model):
    Name=models.CharField(max_length=40)
   
   
   
    
    def __str__(self):
         return f"{self.id} {self.Name}"


class Family(models.Model):
    Name=models.CharField(max_length=60)
    LastName=models.CharField(max_length=60)
    MotherName=models.CharField(max_length=60)
    Age=models.IntegerField(null=True)
    BirthDay=models.DateField(null=True)

    def __str__(self):
        return f"{self.id} {self.Name} {self.LastName} {self.MotherName} {self.Age} {self.BirthDay}"

    
        



