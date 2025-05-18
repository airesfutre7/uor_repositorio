from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.http import FileResponse
import os

# Create your views here.

def home(request):

    return render(request,'home/index.html')

def artigos(request):
    return render(request,'home/artigos.html')

def monografias(request):
    return render(request,'home/monografias.html')

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