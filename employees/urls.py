from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view()),
    path('employees/<uuid:employee_id>/', EmployeeRetrieveUpdateDestroyView.as_view())
]