# accounts/urls.py
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('registro/', views.SignUp.as_view(), name='signup'),
    path('sesion/iniciar/', views.LoginView.as_view(), name='login'),
    path('sesion/cerrar/', views.LogoutView.as_view(), name='logout'),
]
