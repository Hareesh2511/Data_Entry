from django.shortcuts import render
from testapp.models import Employee

def emp_data_view(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'emp.html',my_dict)

# Create your views here.
