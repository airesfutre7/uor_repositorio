from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from users.models import Perfil
from django.http import FileResponse
from django.contrib import messages
import os

# Create your views here.

def home(request):

    return render(request,'home/index.html')

def artigos(request):
    return render(request,'home/artigos.html')

def monografias(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
        monografias = perfil.monografias.all()
        context = {
            'perfil': perfil,
            'monografias': monografias,
        }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request, 'home/monografias.html', context)


def dissertacao(request):
    return render(request,'home/dissertacao.html')

def tese(request):
    return render(request,'home/tese.html')

def faculdade_direito(request):
    return render(request,'home/faculdade_direito.html')

def faculdade_engenharia(request):
    return render(request,'home/faculdade_engenharia.html')

def faculdade_economia(request):
    return render(request,'home/faculdade_economia.html')

def faculdade_gestao(request):
    return render(request,'home/faculdade_gestao.html')

def serve_pdf(request, filename):
    filepath = os.path.join('media/pdfs', filename)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')