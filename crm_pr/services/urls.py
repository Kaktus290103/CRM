from django.urls import path
from .views import services_page, services_table

urlpatterns = [
    path("",services_table, name="services_table"),
    path("",services_page, name="services_page"),
]