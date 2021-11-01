from django.shortcuts import render

# Create your views here.
def tasks_page(request):
    return render(request, "tasks.html",{})