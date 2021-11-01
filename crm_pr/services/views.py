from django.shortcuts import render

# Create your views here.
def services_page(request):
    return render(request, "services.html",{})