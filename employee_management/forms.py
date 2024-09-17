from django import forms
from .models import Employee

# Employee Form for adding new employees
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'address', 'phone_number', 'designation', 'salary', 'short_description']

# Employee Form for updating employees with locked fields
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'short_description', 'designation', 'salary']

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Lock 'designation' and 'salary' fields if the instance already exists (i.e., it's an update)
            self.fields['designation'].disabled = True
            self.fields['salary'].disabled = True
            

