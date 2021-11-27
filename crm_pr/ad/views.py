from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.core import mail
from django.conf import settings
from crm_pr.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.http import HttpResponse
from ad.models import Ad
from ad.forms import AdForm, GetForm
# Create your views here.
def ad_page(request):
    return render(request, "ad.html",{})

def ad_table(request):
    ad = Ad.objects.all()
    form = GetForm()
    tform = AdForm()
    if request.method == "POST":
        form = GetForm(request.POST)
        if form.is_valid():
            form.save()
        tform = AdForm(request.POST)
        if tform.is_valid():
            thema = tform.cleaned_data['thema']
            text =  tform.cleaned_data['text']
            send_mail(f'{thema} от kaktus290103@gmail.com', text,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            with mail.get_connection() as connection:
                EmailMessage(f'{thema} от kaktus290103@gmail.com', text,
                          'kaktus290103@gmail.com', ['kaktus290103@gmail.com'], connection=connection).send()
            return HttpResponse(f'{thema} от kaktus290103@gmail.com {text}',)
    return render(request, "ad.html",{'ad': ad,
                                     'form':form,
                                     'tform': tform })
