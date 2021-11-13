from django.urls import path
from .views import teachers_page, teachers_table
urlpatterns = [
    path("",teachers_page, name="teachers_page"),
    path("",teachers_table, name="teachers_table"),
]