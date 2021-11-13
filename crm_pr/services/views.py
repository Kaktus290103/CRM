from django.shortcuts import render
from services.models import ServiceModel
# Create your views here.
def services_page(request):
    return render(request, "services.html",{})

def services_table(request):
    services = ServiceModel.objects.all()
    return render(request,'./services.html',
                  {'services': services,})