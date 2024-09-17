from django.core.management.base import BaseCommand
from employee_management.models import Employee

class Command(BaseCommand):
    help = 'Update existing records with a default value for the salary field'

    def handle(self, *args, **kwargs):
        employees = Employee.objects.all()
        updated_count = 0

        for employee in employees:
            if employee.salary is None:
                employee.salary = 0.00  # Or any default value you choose
                employee.save()
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} employee records.'))
