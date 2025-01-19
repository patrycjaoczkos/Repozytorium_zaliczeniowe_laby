from django.contrib import admin  # Zmiana tutaj
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),  # To działa, bo admin jest poprawnie zaimportowany
    path('folder_aplikacji/', include('folder_aplikacji.urls')),
    path('accounts/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

