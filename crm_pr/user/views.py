from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/main/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "user/regist.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        redirect('/user/')
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form) 
# Create your views here.
# def regist_view(request):
#     return render(request,"user/regist.html",
#                   {})
class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "user.html"

    # В случае успеха перенаправим на главную.
    success_url = "/main/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")


