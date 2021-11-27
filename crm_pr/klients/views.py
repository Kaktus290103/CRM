from django.shortcuts import render, redirect
from klients.forms import KlientForm
from klients.models import Klients
from django.shortcuts import redirect
import pdb

# Create your views here.
def klients_page(request):
    return render(request, "klients.html",{})

def klients_table(request):
    allklients = Klients.objects.all()
    form = KlientForm()
    if request.method == "POST":
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('klients_table')

    
                        
        #pdb.set_trace()
        
        
    return render(request,'./klients.html',
                  {'allklients': allklients,
                  'form' : form })

    # if request.method == "POST":
    #     form1 = KlientForm(request.POST)
    #     name = request.POST['f_name']
    #     sname = request.POST['s_name']
    #     service = request.POST['servise']
    #     townf = request.POST['town']
    #     schollf = request.POST['school']
    #     telephoneh= request.POST['telephone']
    #     # callf = request.POST['call']
    #     inf = request.POST['another_inf']
    #     statusf = request.POST['status']
    #     istochnickf = request.POST['istochnik']
    #     # Klients.objects.create(f_name = name, 
    #     #                       s_name = sname,
    #     #                       servise  = service,
    #     #                       town = townf,
    #     #                       school = schollf  ,
    #     #                       telephone =  telephoneh,
    #     #                       #call =  callf ,
    #     #                       another_inf = inf  ,
    #     #                       status =  statusf ,
    #     #                       istochnik = istochnickf  ,)
            