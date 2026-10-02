from django import forms
from .models import Computador, pecasDeComputador

class ComputadorForm(forms.ModelForm):
    
    class Meta:
        model = Computador
        fields = ['nome',]
class pecasDeComputadorForm(forms.ModelForm):
    class Meta:
        model = pecasDeComputador
        fields = '__all__'
        
        