# accounts/urls.py
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('registro/', views.SignUp.as_view(), name='signup'),
    path('login/', views.LoginRegular.as_view(), name='login'),
]
