from django.urls import path, re_path
from .views import klients_page
# from klients.views import klients_forms
from . import views
urlpatterns = [
    path("table/", views.klients_table, name='klients_table'),
    #path("table/add", klients_forms, name='klients_forms'),
    
    path("",klients_page, name="klients_page"),
    
    
]