from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/criar-computador/',views.criar_computador, name='criar_computador' ),
    path('dashboard/seus-computadores', views.seucomputador, name='seus_computadores')
    
]