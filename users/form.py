# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Perfil, Monografia, Tese, Artigo, Livro, Dissertacao

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
        fields = ['titulo', 'resumo', 'faculdade', 'ficheiro']
        
        widgets = {
           
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da monografia'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da monografia'
            }),
            'faculdade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }

class TeseForm(forms.ModelForm):
    class Meta:
        model = Tese
        fields = ['titulo', 'resumo', 'faculdade', 'ficheiro']
        
        widgets = {
        
            
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da tese'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da tese'
            }),
            'faculdade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }

class DissertacaoForm(forms.ModelForm):
    class Meta:
        model = Dissertacao
        fields = ['titulo', 'resumo', 'faculdade', 'ficheiro']
        
        widgets = {
        
           
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da dissertação'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da dissertação'
            }),
            'faculdade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'resumo', 'faculdade', 'ficheiro']
        
        widgets = {
        
           
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da artigo'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da artigo'
            }),
            'faculdade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'resumo', 'faculdade', 'ficheiro']
        
        widgets = {
        
           
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da livro'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da livro'
            }),
            'faculdade': forms.Select(attrs={
                'class': 'form-control'
            }),

            'ficheiro': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile01'
            }),

               
        }