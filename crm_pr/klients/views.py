from django.shortcuts import render

# Create your views here.
def klients_page(request):
    return render(request, "klients.html",{})