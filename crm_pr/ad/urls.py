from django.urls import path
from .views import ad_page
urlpatterns = [
    path("",ad_page, name="ad_page"),
]