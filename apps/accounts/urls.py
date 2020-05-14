from django.urls import path

from apps.accounts.views import perfil

urlpatterns = [
    path('perfil', perfil, name='perfil'),

]
