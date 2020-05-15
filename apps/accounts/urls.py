from django.urls import path

from apps.accounts.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_page, name='register'),
    path('perfil/', perfil, name='perfil'),

]
