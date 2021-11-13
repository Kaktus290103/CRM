from django.shortcuts import render
from teachers.models import Teachers
# Create your views here.
def teachers_page(request):
    return render(request, "teachers.html",{})

def teachers_table(request):
    teachers = Teachers.objects.all()
    return render(request,'./teachers.html',
                  {'teachers': teachers,})