from django.urls import path
from tasks.views import tasks_page, tasks_table
urlpatterns = [
    path("",tasks_table, name="tasks_table"),
    #path("",tasks_page, name="tasks_page"),
]