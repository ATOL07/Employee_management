from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm



def homepage(request):
    employees = Employee.objects.all()
    return render(request, 'homepage.html', {'employees': employees})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_profile(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_profile.html', {'employee': employee})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

        if employee.pk:  # Check if the employee object exists (i.e., it's not a new object)
            form.fields['salary'].widget.attrs['readonly'] = True
            form.fields['designation'].widget.attrs['readonly'] = True

            
    return render(request, 'update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'confirm_delete.html', {'employee': employee})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee to the database
            return redirect('employee_list')  # Redirect to the employee list view after adding
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

