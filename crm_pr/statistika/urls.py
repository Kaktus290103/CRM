from django.urls import path
from .views import statistika_page
urlpatterns = [
    path("",statistika_page, name="statistika_page"),
]