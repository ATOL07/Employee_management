from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'name', 'designation', 'salary']  # Display these fields in the admin
    fields = ['employee_id', 'name', 'address', 'phone_number', 'short_description', 'designation', 'salary']  # Make sure these fields appear in the form

admin.site.register(Employee, EmployeeAdmin)
