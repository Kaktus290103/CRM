from django.urls import path
from tasks.views import task_view, tasks_table
urlpatterns = [
    path("",tasks_table, name="tasks_table"),
    path("form/",task_view, name="tasks_view"),
    #path("",tasks_page, name="tasks_page"),
]