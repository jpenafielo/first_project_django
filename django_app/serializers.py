from rest_framework import serializers 
from .models import CustomerBar, EmployeesBar


class CustomerBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBar
        fields = ( 'id', 'name', 'lastName', 'email', 'age','createdAt')


class EmployeesBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesBar
        fields = ( 'id', 'name', 'lastName', 'email', 'age', 'position', 'salary', 'yearsInCompany')
        