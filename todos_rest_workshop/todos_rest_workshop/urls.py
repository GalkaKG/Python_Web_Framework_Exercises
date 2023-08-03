from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('todos_rest_workshop.todos_api.urls')),
    path('api/auth/', include('todos_rest_workshop.accounts.urls')),
]
