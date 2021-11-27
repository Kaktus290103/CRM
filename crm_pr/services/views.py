from django.shortcuts import render, redirect
from services.models import ServiceModel
from services.forms import ServiceForm 
from services.forms import TeachersForm
import pdb
# Create your views here.
def services_page(request):
    return render(request, "services.html",{})

def services_table(request):
    services = ServiceModel.objects.all()
    form = ServiceForm()
    tform = TeachersForm()
    if request.method == "POST":
        form = ServiceForm(request.POST)
        tform = TeachersForm(request.POST)
        if form.is_valid():
            form.save()
        if tform.is_valid():
            tform.save()
            
            return redirect('services_table')
    return render(request,'./services.html',
                  {'services': services,
                  'form': form,
                  'tform': tform, })