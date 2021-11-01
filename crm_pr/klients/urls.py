from django.urls import path
from .views import klients_page
urlpatterns = [
    path("",klients_page, name="klients_page"),
]