from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django_app.models import CustomerBar
from .serializers import CustomerBarSerializer ,EmployeesBarSerializer
from django.utils import timezone

@csrf_exempt
def CustomerBarView (request):
    if request.method == 'GET':
        customer = CustomerBar.objects.all()
        customerSerializer = CustomerBarSerializer(customer, many=True)
        return JsonResponse(customerSerializer.data, safe=False)
    if request.method == 'POST':
        customerData = JSONParser().parse(request)
        customerData["createdAt"] = timezone.now().date()
        customerSerializer = CustomerBarSerializer(data=customerData)
        if customerSerializer.is_valid():
            customerSerializer.save()
            return JsonResponse('Customer added succesfully', safe=False)
        else:
            return JsonResponse('Chat failed to add', safe=False)