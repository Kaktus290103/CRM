from django.urls import path
from user.views import RegisterFormView, LoginFormView, LogoutView
urlpatterns = [
    path("",LoginFormView.as_view(), name="user_view"),
    path("registration/",RegisterFormView.as_view(),name='regist_view'),
    # path("",user_view, name="user_view"),
]