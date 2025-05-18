from django.shortcuts import render, redirect

from .form import CadastroForm, ProfileForm
from django.contrib import messages
from .models import Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):

    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta de {username} criada com sucesso ')
            return redirect('login')
    else:
        form = CadastroForm()

    return render(request, 'users/signup.html', {'form': form})

@login_required
def edit_perfil(request):
    try:
        perfil_instance = Perfil.objects.get(user=request.user)

        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=perfil_instance)
            if form.is_valid():
                form.save()
                nome = form.cleaned_data.get('nome')
                messages.success(request, f'Conta de {nome} atualizada com sucesso')
                return redirect('home')
        else:
            form = ProfileForm(instance=perfil_instance)

        return render(request, 'users/edit_perfil.html', {'form': form})
    
    except Perfil.DoesNotExist:
        messages.error(request, "Você ainda não tem um perfil. Crie um primeiro.")
        return redirect('home')  # or redirect to a create-perfil page

   

@login_required
def perfil(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request, 'users/perfil.html', {'perfil': perfil})
