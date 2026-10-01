from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComputadorForm
from .models import Computador


def home(request):
    return render(request, 'computador/home.html')
   
@login_required()
def dashboard(request):
    return render(request, 'computador/dashboard.html')

@login_required()
def criar_computador(request):
    if request.method == 'POST':
        form = ComputadorForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ComputadorForm()
    
    context = {
        'form':form
    }
    return render(request, 'computador/criar_computador.html', context)
    
@login_required()
def seucomputador(request):
    
    pc = Computador.objects.all()
    context = {
        'pc':pc
        }
    return render(request, 'computador/seus_computadores.html', context)
