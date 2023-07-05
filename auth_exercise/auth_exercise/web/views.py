from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, login, authenticate, get_user_model, mixins
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works'


class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(LoginView):
    template_name = 'login.html'
    # extra_context = {'title': 'login', 'link_title': 'register'}


class LogoutUserView(views.View):
    pass


UserModel = get_user_model()


@login_required
def func_view(request):
    pass


class UsersListView(views.ListView, mixins.LoginRequiredMixin):
    model = UserModel
    template_name = 'users_list.html'
