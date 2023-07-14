from django.urls import path

from auth_exercise.web.views import RegisterUserView, LoginUserView, UsersListView, PaginateView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LoginUserView.as_view(), name='logout_user'),
    path('', UsersListView.as_view(), name='users_list'),
    path('paginate/', PaginateView.as_view(), name='paginate'),
)

# Password:  pAss789$
