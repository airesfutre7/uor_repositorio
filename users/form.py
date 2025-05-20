# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Perfil, Monografia

class CadastroForm(UserCreationForm):
   
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['imagem', 'nome', 'sobrenome', 'sobre']
        
        widgets = {
                'imagem': forms.ClearableFileInput(attrs={
                    'class': 'custom-file-input',
                    'id': 'inputGroupFile01'
                }),

                'nome': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'nome ..'
                }),

                'sobrenome': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'sobrenome ..'
                }),
                'sobre': forms.Textarea(attrs={
                    'class': 'form-control',
                    'rows': 4,  # Optional: control height
                    'placeholder': 'Escreva algo sobre você...'  # Optional
            }),
            }


class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografia
        fields = ['autor', 'titulo', 'resumo', 'ficheiro']
        
        widgets = {
        
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autor da monografia'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da monografia'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da monografia'
            }),
            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }