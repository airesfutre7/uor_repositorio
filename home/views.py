from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from users.models import Perfil
from django.http import FileResponse
from django.contrib import messages
import os
from django.shortcuts import get_object_or_404
from users.models import Artigo, Perfil, Monografia, Tese, Livro, Dissertacao


# Create your views here.

def home(request):

    return render(request,'home/index.html')

def artigo_list(request):
    try:
       #perfil = Perfil.objects.get(user=request.user)
        #artigos = perfil.artigo.all()
        artigos = Artigo.objects.all()
        context = {
           # 'perfil': perfil,
            'artigos': artigos,
        }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request, 'home/artigo_list.html', context)

def artigo(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   artigo = get_object_or_404(Artigo, pk=pk)
   
   return render(request, 'home/artigos.html', {'artigo': artigo})

def monografias(request):
    try:
        #perfil = Perfil.objects.get(user=request.user)
        #monografias = perfil.monografias.all()
        monografias = Monografia.objects.all()
        context = {
            #'perfil': perfil,
            'monografias': monografias,
        }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request, 'home/monografias.html', context)

def livro(request):
    try:
        #perfil = Perfil.objects.get(user=request.user)
        #livros = perfil.livro.all()
        livros = Livro.objects.all()
        context = {
           # 'perfil': perfil,
            'livros': livros,
        }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request, 'home/livro.html', context)

def dissertacao(request):
    try:
        #perfil = Perfil.objects.get(user=request.user)
        #dissertacoes = perfil.dissertacoes.all()
        dissertacoes = Dissertacao.objects.all()
        context = {
            #'perfil': perfil,
            'dissertacoes': dissertacoes,
    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request, 'home/dissertacao.html', context)

def tese(request):
    try:
       # perfil = Perfil.objects.get(user=request.user)
        #teses = perfil.tese.all()
        teses = Tese.objects.all()
        context = {
            #'perfil': perfil,
            'teses': teses,
    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request, 'home/tese.html', context)

def faculdade_direito(request):
    try:
       # perfil = Perfil.objects.get(user=request.user)
        #teses = perfil.tese.all()
        teses = Tese.objects.filter(faculdade='dir')
        monografias = Monografia.objects.filter(faculdade='dir')
        teses = Tese.objects.filter(faculdade='dir')
        livros = Livro.objects.filter(faculdade='dir')
        artigos = Artigo.objects.filter(faculdade='dir')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_direito.html', context)

def faculdade_engenharia(request):

    try:
       
        teses = Tese.objects.filter(faculdade='eng')
        monografias = Monografia.objects.filter(faculdade='eng')
        teses = Tese.objects.filter(faculdade='eng')
        livros = Livro.objects.filter(faculdade='eng')
        artigos = Artigo.objects.filter(faculdade='eng')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request,'home/faculdade_engenharia.html', context)

def faculdade_economia(request):
    try:
  
        teses = Tese.objects.filter(faculdade='econ')
        monografias = Monografia.objects.filter(faculdade='econ')
        teses = Tese.objects.filter(faculdade='econ')
        livros = Livro.objects.filter(faculdade='econ')
        artigos = Artigo.objects.filter(faculdade='econ')
        context = {
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_economia.html', context)

def faculdade_gestao(request):
    try:
    
        teses = Tese.objects.filter(faculdade='ges')
        monografias = Monografia.objects.filter(faculdade='ges')
        teses = Tese.objects.filter(faculdade='ges')
        livros = Livro.objects.filter(faculdade='ges')
        artigos = Artigo.objects.filter(faculdade='ges')
        context = {
          
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_gestao.html', context)

def serve_pdf(request, filename):
    filepath = os.path.join('media/pdfs', filename)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')