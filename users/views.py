from django.shortcuts import render, redirect

from .form import CadastroForm, ProfileForm, MonografiaForm, TeseForm, DissertacaoForm, ArtigoForm, LivroForm
from django.contrib import messages
from .models import Perfil
from django.contrib.auth.decorators import login_required
from pdf2image import convert_from_path
from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO

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
        monografias = perfil.monografias.all()
        teses = perfil.tese.all()
        #dissertacoes = perfil.dissertacaos.all()
        artigos = perfil.artigo.all()
        livros = perfil.livro.all()
        context = {
            'perfil': perfil,
            'monografias': monografias,
            'artigos': artigos,
            #'dissertacoes': dissertacoes,
            'teses': teses,
            'livros': livros,
        }
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado.")
        return redirect('home')  

    return render(request, 'users/perfil.html', context)


def monografia(request):
    if request.method == 'POST':
        form = MonografiaForm(request.POST, request.FILES)
        if form.is_valid():
            monografia = form.save(commit=False)
            monografia.autor = request.user.perfil  # ✅ set the author!
            monografia.save()

            # Convert first page of PDF to image
            pdf_path = monografia.ficheiro.path
            pages = convert_from_path(pdf_path, first_page=1, last_page=1,
                                      poppler_path=r'C:\Users\aires.conceicao\Downloads\Release-24.08.0-0 (1)\poppler-24.08.0\Library\bin'
                                      )
            if pages:
                image = pages[0]
                image_io = BytesIO()
                image.save(image_io, format='JPEG')

                # Save to model
                monografia.capa.save(
                    f'{os.path.splitext(os.path.basename(pdf_path))[0]}_capa.jpg',
                    ContentFile(image_io.getvalue()),
                    save=True
                )

            return redirect('perfil')
    else:
        form = MonografiaForm()
    return render(request, 'users/monografia_form.html', {'form': form})

def tese(request):
    if request.method == 'POST':
        form = TeseForm(request.POST, request.FILES)
        if form.is_valid():
            tese = form.save(commit=False)
            tese.autor = request.user.perfil  # ✅ set the author!
            tese.save()

            # Convert first page of PDF to image
            pdf_path = tese.ficheiro.path
            pages = convert_from_path(pdf_path, first_page=1, last_page=1,
                                      poppler_path=r'C:\Users\aires.conceicao\Downloads\Release-24.08.0-0 (1)\poppler-24.08.0\Library\bin'
                                      )
            if pages:
                image = pages[0]
                image_io = BytesIO()
                image.save(image_io, format='JPEG')

                # Save to model
                tese.capa.save(
                    f'{os.path.splitext(os.path.basename(pdf_path))[0]}_capa.jpg',
                    ContentFile(image_io.getvalue()),
                    save=True
                )

            return redirect('perfil')
    else:
        form = TeseForm()
    return render(request, 'users/tese_form.html', {'form': form})

def dissertacao(request):
    if request.method == 'POST':
        form = DissertacaoForm(request.POST, request.FILES)
        if form.is_valid():
            dissertacao = form.save(commit=False)
            dissertacao.autor = request.user.perfil  # ✅ set the author!
            dissertacao.save()

            # Convert first page of PDF to image
            pdf_path = dissertacao.ficheiro.path
            pages = convert_from_path(pdf_path, first_page=1, last_page=1,
                                      poppler_path=r'C:\Users\aires.conceicao\Downloads\Release-24.08.0-0 (1)\poppler-24.08.0\Library\bin'
                                      )
            if pages:
                image = pages[0]
                image_io = BytesIO()
                image.save(image_io, format='JPEG')

                # Save to model
                dissertacao.capa.save(
                    f'{os.path.splitext(os.path.basename(pdf_path))[0]}_capa.jpg',
                    ContentFile(image_io.getvalue()),
                    save=True
                )

            return redirect('perfil')
    else:
        form = DissertacaoForm()
    return render(request, 'users/dissertacao_form.html', {'form': form})

def artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo= form.save(commit=False)
            artigo.autor = request.user.perfil  # ✅ set the author!
            artigo.save()

            # Convert first page of PDF to image
            pdf_path = artigo.ficheiro.path
            pages = convert_from_path(pdf_path, first_page=1, last_page=1,
                                      poppler_path=r'C:\Users\aires.conceicao\Downloads\Release-24.08.0-0 (1)\poppler-24.08.0\Library\bin'
                                      )
            if pages:
                image = pages[0]
                image_io = BytesIO()
                image.save(image_io, format='JPEG')

                # Save to model
                artigo.capa.save(
                    f'{os.path.splitext(os.path.basename(pdf_path))[0]}_capa.jpg',
                    ContentFile(image_io.getvalue()),
                    save=True
                )

            return redirect('perfil')
    else:
        form = ArtigoForm()
    return render(request, 'users/artigo_form.html', {'form': form})

def livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro= form.save(commit=False)
            livro.autor = request.user.perfil  # ✅ set the author!
            livro.save()

            # Convert first page of PDF to image
            pdf_path = livro.ficheiro.path
            pages = convert_from_path(pdf_path, first_page=1, last_page=1,
                                      poppler_path=r'C:\Users\aires.conceicao\Downloads\Release-24.08.0-0 (1)\poppler-24.08.0\Library\bin'
                                      )
            if pages:
                image = pages[0]
                image_io = BytesIO()
                image.save(image_io, format='JPEG')

                # Save to model
                livro.capa.save(
                    f'{os.path.splitext(os.path.basename(pdf_path))[0]}_capa.jpg',
                    ContentFile(image_io.getvalue()),
                    save=True
                )

            return redirect('perfil')
    else:
        form = LivroForm()
    return render(request, 'users/livro_form.html', {'form': form})