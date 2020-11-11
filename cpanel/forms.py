from django import forms
from .models import RegistrationData

#formulario de cadastro
class RegistrationForm(forms.Form):
    nome = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'Nome',
                                'required':'True'
                            }))

    telefone = forms.CharField(max_length=20,
                            widget=forms.NumberInput(attrs={
                                'class':'form-control',
                                'placeholder':'Telefone',
                                'required':'True'
                            }))

    email = forms.CharField(max_length=50,
                            widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'E-mail',
                                'required':'True'
                            }))

    atuacao = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'Atuação',
                                'required':'True'
                            }))
    termos_servico = forms.CharField(widget = forms.CheckboxInput(attrs={'required':'True'})) 

 