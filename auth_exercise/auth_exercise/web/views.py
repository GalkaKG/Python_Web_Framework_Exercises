from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, login, authenticate, get_user_model, mixins
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.middleware.csrf import get_token


from auth_exercise.web.forms import ArticleBaseForm
from auth_exercise.web.serializers import ArticleSerializers
from auth_exercise.web.models import Article


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
    template_name = 'web/register.html'
    # Static way to get form
    form_class = RegisterUserForm

    # Static way for providing success url
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    # Dynamic way for providing success url
    def get_success_url(self):
        pass

    # Dynamic way to get form
    def get_form_class(self):
        pass


class LoginUserView(LoginView):
    template_name = 'web/login.html'
    # extra_context = {'title': 'login', 'link_title': 'register'}


class LogoutUserView(views.View):
    pass


UserModel = get_user_model()


@login_required
def func_view(request):
    pass


class ViewWithPermission(mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'web/users_list.html'


class UsersListView(views.ListView, mixins.LoginRequiredMixin, APIView):
    model = UserModel
    template_name = 'web/users_list.html'

    # Login URL only for this view
    # login_url = 'custom-login-url'


class PaginateView(views.ListView):
    template_name = 'web/paginate.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 5


class ArticleView(APIView):
    template_name = 'web/create-article.html'

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        form = ArticleBaseForm()
        return render(request, self.template_name, {'articles': serializer.data, 'form': form})

    def post(self, request):
        form = ArticleBaseForm(request.POST)
        if form.is_valid():
            article = form.save()
            serializer = ArticleSerializers(article)
            response_data = {
                'message': 'Article created successfully.',
                'data': serializer.data,
            }
            # return Response(response_data, status=status.HTTP_201_CREATED)
            return redirect('paginate')
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializers(articles, many=True)
            return render(request, self.template_name, {'articles': serializer.data, 'form': form})

