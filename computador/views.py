from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.contrib import messages
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
    success_url = reverse_lazy('criar_computador')

    # verificar se o formulario foi valido e ativar o message para aplicar o modal
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)

        messages.success(
            self.request,
            'Computador cadastrado com sucesso'
        )
        return response


class SeusComputadoresView(LoginRequiredMixin, ListView):
    model = Computador
    template_name = 'computador/seus_computadores.html'
    context_object_name = 'pc'
    #filtro pra pegar os pc do usuario logado
    def get_queryset(self):
        return Computador.objects.filter(usuario=self.request.user)


class DeletarComputadorView(LoginRequiredMixin, DeleteView):
    model = Computador
    success_url = reverse_lazy('seus_computadores')
    #setar metodo post p/ delete
    http_method_names = ['post']

    #filtro pra pegar os pc do usuario logado
    def get_queryset(self):
        return Computador.objects.filter(usuario=self.request.user)


class EditarSeuComputadorView(LoginRequiredMixin, CreateView):
    model = pecasDeComputador
    form_class = pecasDeComputadorForm
    template_name = 'computador/editar_seu_computador.html'
    success_url = reverse_lazy('editar_seu_computador')

    # serve para filtar apenas pelos usuario logado
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['computador'].queryset = Computador.objects.filter(
            usuario=self.request.user
        )
        return form

    # verificar se o formulario foi valido e ativar o message para aplicar o modal
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Peças de computador cadastradas com sucesso'
        )
        return response
