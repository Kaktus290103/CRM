import pdb
from django.shortcuts import render, redirect
# from django.views.decorator.csrf import crsf_exempt
from tasks.forms import TaskForm
from tasks.models import Tasks
# Create your views here.
def tasks_page(request):
    return render(request, "tasks.html",{})

def tasks_table(request):
    tasks = Tasks.objects.all()
    if request.method == "POST":
        print(request.POST)
        check = request.POST.get("check")
        task_id = request.POST.get("task_id", False)
        pdb.set_trace()
        task = Tasks.objects.get(pk=task_id)
        task.check = check
        task.save()
        
        return "{\"result\": 10}"
        
        #return redirect('/tasks/')
    return render(request,'tasks.html',
                  {'tasks': tasks,})

def check_view(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            if request.POST["check"]:
                tasks = Tasks.objects.all()
                tasks.check = True
