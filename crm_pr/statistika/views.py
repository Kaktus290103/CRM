from django.shortcuts import render

# Create your views here.
def statistika_page(request):
    return render(request, "statistika.html",{})