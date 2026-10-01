from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Caminho de Login usando o Login do próprio django, configuração de rotas após login configuradas no main/settings.py
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('registrar/', views.registrar, name = 'registrar'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name = 'logout')
]
