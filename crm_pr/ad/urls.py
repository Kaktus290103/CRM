from django.urls import path
from ad.views import ad_page, ad_table
urlpatterns = [
    path("",ad_table, name="ad_table"),
    path("",ad_page, name="ad_page"),
]
