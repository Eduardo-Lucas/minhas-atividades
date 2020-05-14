from django.urls import path

from apps.accounts.views import login_view, logout_view, register_page

urlpatterns = [
    path('register', register_page, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
