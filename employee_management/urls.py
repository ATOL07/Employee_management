
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('employee/list/', views.employee_list, name='employee_list'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/<int:pk>/', views.employee_profile, name='employee_profile'),
    path('employee/<int:pk>/edit/', views.update_employee, name='update_employee'),
    path('employee/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]
