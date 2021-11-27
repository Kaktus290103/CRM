from django.urls import path
from .views import statistika_page, view_func
urlpatterns = [
    path("",view_func, name="table"),
    #path("",statistika_page, name="statistika_page"),
]