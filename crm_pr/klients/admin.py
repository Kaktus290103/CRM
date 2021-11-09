from django.contrib import admin
from .models import Klients, StatusKlienta, Istochnik

admin.site.register(StatusKlienta)
admin.site.register(Istochnik)
admin.site.register(Klients)