from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from .forms import ComputadorForm, pecasDeComputadorForm
from .models import Computador, pecasDeComputador


class HomeView(TemplateView):
    template_name = 'computador/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'computador/dashboard.html'


class CriarComputadorView(LoginRequiredMixin, CreateView):
    model = Computador
    form_class = ComputadorForm
    template_name = 'computador/criar_computador.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class SeusComputadoresView(LoginRequiredMixin, ListView):
    model = Computador
    template_name = 'computador/seus_computadores.html'
    context_object_name = 'pc'

    def get_queryset(self):
        return Computador.objects.filter(usuario=self.request.user)
class EditarSeuComputadorView(LoginRequiredMixin, CreateView):
    model = pecasDeComputador
    form_class = pecasDeComputadorForm
    template_name = 'computador/editar_seu_computador.html'
    success_url = reverse_lazy('dashboard')
    
    # serve para filtar apenas pelos usuario logado
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['computador'].queryset = Computador.objects.filter(
            usuario=self.request.user
        )

        return form
    
    