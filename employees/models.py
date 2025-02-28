from django.db import models
from uuid import uuid4

class GenderChoices(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHERS = 'O', 'Others'

class Employee(models.Model):
    employee_id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    gender = models.CharField(choices=GenderChoices, max_length=1)

    class Meta:
        db_table = 'Employee'
