# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Perfil

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

    