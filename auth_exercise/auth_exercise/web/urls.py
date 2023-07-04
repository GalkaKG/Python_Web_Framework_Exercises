from django.urls import path

from auth_exercise.web.views import RegisterUserView, LoginUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LoginUserView.as_view(), name='logout_user'),
)
