from .models import CustomerBar, EmployeesBar
from rest_framework import viewsets, permissions
from .serializers import CustomerBarSerializer ,EmployeesBarSerializer

class CustomerBarViewSet(viewsets.ModelViewSet):
    queryset = CustomerBar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerBarSerializer


class EmployeesBarViewSet(viewsets.ModelViewSet):
    queryset = EmployeesBar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeesBarSerializer 
    