from django.urls import path

from todos_rest_workshop.accounts.views import ApiRegisterUserView, ApiLoginUserView, ApiLogoutUserView

urlpatterns = (
    path('register/', ApiRegisterUserView.as_view(), name='api register view'),
    path('login/', ApiLoginUserView.as_view(), name='api login view'),
    path('logout/', ApiLogoutUserView.as_view(), name='api logout view'),
)
