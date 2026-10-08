from django.urls import path
from .views import HomeView, DashboardView, CriarComputadorView, SeusComputadoresView, EditarSeuComputadorView, DeletarComputadorView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/criar-computador/',CriarComputadorView.as_view(), name='criar_computador' ),
    path('dashboard/seus-computadores', SeusComputadoresView.as_view(), name='seus_computadores'),
    path('dashboard/editar-computador', EditarSeuComputadorView.as_view(), name='editar_seu_computador'),
    path('dashboard/<int:pk>/excluir', DeletarComputadorView.as_view(), name='deletar_computador')
]