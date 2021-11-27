import pdb
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
from tasks.forms import TaskForm
from tasks.models import Tasks
# Create your views here.
def tasks_page(request):
    return render(request, "tasks.html",{})

@csrf_exempt
def tasks_table(request):
    if request.method == "POST":
        try:
            check = True if request.POST["check"] == "true" else False
            task_id = int(request.POST["task_id"])
        except KeyError:
            return HttpResponseServerError("Keys not found")
        task = Tasks.objects.get(pk=task_id)
        task.check = check
        task.save()
        #tasks = Tasks.objects.all()
        
        
    tasks = Tasks.objects.all()
    #pdb.set_trace() 
    return render(
        request,
        "tasks.html",
        {
            "tasks": tasks,
        },
    )

def task_view(request):
    form = TaskForm()
    tasks = Tasks.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks_table')
    return render(
        request,
        "tasks/addtask.html",
        {
            "tasks": tasks,
            "form": form,
        },
    )

# def check_view(request):
#     form = TaskForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             if request.POST["check"]:
#                 tasks = Tasks.objects.all()
#                 tasks.check = True
