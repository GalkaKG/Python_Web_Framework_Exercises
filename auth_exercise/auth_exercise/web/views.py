from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import forms as auth_forms


class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = auth_forms.UserCreationForm


class LoginUserView(views.View):
    pass


class LogoutUserView(views.View):
    pass
