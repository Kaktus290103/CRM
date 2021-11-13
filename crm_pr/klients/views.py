from django.shortcuts import render

from klients.models import Klients

# Create your views here.
def klients_page(request):
    return render(request, "klients.html",{})

def klients_table(request):
    allklients = Klients.objects.all()
    return render(request,'./klients.html',
                  {'allklients': allklients,})