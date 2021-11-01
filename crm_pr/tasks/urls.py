from django.urls import path
from .views import tasks_page
urlpatterns = [
    path("",tasks_page, name="tasks_page"),
]