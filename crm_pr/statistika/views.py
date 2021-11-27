from django.shortcuts import render
from django.db.models import Count
import datetime
from qsstats import QuerySetStats
from klients.models import Klients
import pdb
# Create your views here.
def statistika_page(request):
    return render(request, "statistika.html",{})



def view_func(request):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)

    queryset = Klients.objects.all()
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, date_field='created', aggregate=Count('id'))
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='days')
    return render(request,'statistika.html', {'values': values})