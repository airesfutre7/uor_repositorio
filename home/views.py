from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from users.models import Perfil
from django.http import FileResponse
from django.contrib import messages
import os
from django.shortcuts import get_object_or_404
from users.models import Artigo, Perfil, Monografia, Tese, Livro, Dissertacao
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    artigos = Artigo.objects.order_by('-date')[:3]  # Latest 3 by upload date
    
    return render(request,'home/index.html', {'artigos': artigos})

@login_required
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

@login_required
def artigo(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   artigo = get_object_or_404(Artigo, pk=pk)
  
   return render(request, 'home/artigos.html', {'artigo': artigo})

@login_required
def monografia_view(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   monografia = get_object_or_404(Monografia, pk=pk)
  
   return render(request, 'home/monografia_view.html', {'monografia': monografia})

@login_required
def tese_view(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   tese = get_object_or_404(Tese, pk=pk)
  
   return render(request, 'home/tese_view.html', {'tese': tese})

@login_required
def livro_view(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   livro = get_object_or_404(Livro, pk=pk)
  
   return render(request, 'home/livro_view.html', {'livro': livro})

@login_required
def dissertacao_view(request, pk ):
    #autor = get_object_or_404(Perfil, id=autor_id)
    #artigo = get_object_or_404(Artigo, id=artigo_id, autor=autor)
    
   dissertacao = get_object_or_404(Dissertacao, pk=pk)
  
   return render(request, 'home/dissertacao_view.html', {'dissertacao': dissertacao})

@login_required
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
@login_required
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

@login_required
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

@login_required
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

@login_required
def faculdade_direito(request):
    try:
       # perfil = Perfil.objects.get(user=request.user)
        #teses = perfil.tese.all()
        teses = Tese.objects.filter(faculdade='dir')
        monografias = Monografia.objects.filter(faculdade='dir')
        teses = Tese.objects.filter(faculdade='dir')
        livros = Livro.objects.filter(faculdade='dir')
        artigos = Artigo.objects.filter(faculdade='dir')
        dissertacoes = Dissertacao.objects.filter(faculdade='dir')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos,
            'dissertacoes': dissertacoes

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_direito.html', context)

@login_required
def faculdade_engenharia(request):

    try:
       
        teses = Tese.objects.filter(faculdade='eng')
        monografias = Monografia.objects.filter(faculdade='eng')
        teses = Tese.objects.filter(faculdade='eng')
        livros = Livro.objects.filter(faculdade='eng')
        artigos = Artigo.objects.filter(faculdade='eng')
        dissertacoes = Dissertacao.objects.filter(faculdade='eng')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos,
            'dissertacoes': dissertacoes

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  
    
    return render(request,'home/faculdade_engenharia.html', context)

@login_required
def faculdade_economia(request):
    try:
  
        teses = Tese.objects.filter(faculdade='econ')
        monografias = Monografia.objects.filter(faculdade='econ')
        teses = Tese.objects.filter(faculdade='econ')
        livros = Livro.objects.filter(faculdade='econ')
        artigos = Artigo.objects.filter(faculdade='econ')
        dissertacoes = Dissertacao.objects.filter(faculdade='econ')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos,
            'dissertacoes': dissertacoes

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_economia.html', context)

@login_required
def faculdade_gestao(request):
    try:
    
        teses = Tese.objects.filter(faculdade='ges')
        monografias = Monografia.objects.filter(faculdade='ges')
        teses = Tese.objects.filter(faculdade='ges')
        livros = Livro.objects.filter(faculdade='ges')
        artigos = Artigo.objects.filter(faculdade='ges')
        dissertacoes = Dissertacao.objects.filter(faculdade='ges')
        context = {
            #'perfil': perfil,
            'teses': teses,
            'monografias': monografias,
            'teses': teses,
            'livros': livros,
            'artigos': artigos,
            'dissertacoes': dissertacoes

    }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request,'home/faculdade_gestao.html', context)

@login_required
def serve_pdf(request, filename):
    filepath = os.path.join('media/pdfs', filename)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')