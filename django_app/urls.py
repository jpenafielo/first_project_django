from rest_framework import routers
from .api import CustomerBarViewSet, EmployeesBarViewSet

router = routers.DefaultRouter()
#router.register('bar/customers', CustomerBarView, 'barServices')
router.register('bar/employees', EmployeesBarViewSet, 'barServices')


urlpatterns =  router.urls
