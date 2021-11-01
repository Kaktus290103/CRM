from django.shortcuts import render

# Create your views here.
def ad_page(request):
    return render(request, "ad.html",{})