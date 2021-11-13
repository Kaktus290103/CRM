from django.urls import path, re_path
from .views import klients_page
from . import views
urlpatterns = [
    path("",klients_page, name="klients_page"),
    re_path(r'^$', views.klients_table, name='klients_table'),
]