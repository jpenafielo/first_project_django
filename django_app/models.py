from django.db import models
from django.utils import timezone

class CustomerBar(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    createdAt =  models.DateField(timezone.now)

    def __str__(self):
        return self.name
    
class EmployeesBar(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    yearsInCompany = models.IntegerField()
    
    

    def __str__(self):
        return self.name
