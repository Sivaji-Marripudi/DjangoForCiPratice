from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'