
from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    short_description = models.TextField()
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add default value here

    def __str__(self):
        return self.name
