from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

@login_required(login_url='/logar/')
def cadastrar_vacina(request):
    if request.user.is_staff != 1:
        return redirect(exibir_vacinas)
    if request.method == 'POST': # Se o método for POST
        form = FormVacina(request.POST) # Pegamos o formulário preenchido
        if form.is_valid(): # Validamos
            form.save() # Salvamos no banco de dados
    form = FormVacina()
    context = { # Dicionário com todas as variáveis e valores que serão passados para o html
        'form': form
    }
    return render(request, 'cadastrar_vacina.html', context)

def exibir_vacinas(request):
    vacinas = Vacina.objects.all()
    context = {
        'vacinas': vacinas,
    }
    return render(request, 'vacinas.html', context)

@login_required(login_url='/logar/')
def editar_vacina(request, id_vacina):
    if request.user.is_staff != 1:
        return redirect(exibir_vacinas)
    vacina = Vacina.objects.get(id=id_vacina)
    if request.method == 'POST': 
        form = FormVacina(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect(exibir_vacinas)
    form = FormVacina(instance=vacina)
    context = {
        'form': form,
        'vacina': vacina
    }
    return render(request, 'editar_vacina.html', context)

@login_required(login_url='/logar/')
def excluir_vacina(request, id_vacina):
    if request.user.is_staff != 1:
        return redirect(exibir_vacinas)
    vacina = Vacina.objects.get(id=id_vacina)
    vacina.delete()

    return redirect(exibir_vacinas)

@login_required(login_url='/logar/')
def cadastrar_anuncio(request):
    if request.method == 'POST':
        form = FormAnuncio(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
    form = FormAnuncio()
    context = {
        'form': form
    }
    return render(request, 'cadastrar_anuncio.html', context)

def exibir_anuncios(request):
    anuncios = Anuncio.objects.all()
    context = {
        'anuncios': anuncios
    }
    return render(request, 'anuncios.html', context)

@login_required(login_url='/logar/')
def editar_anuncio(request, id_anuncio):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    if anuncio.usuario != request.user:
        return redirect(exibir_anuncios)
    if request.method == 'POST': 
        form = FormAnuncio(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect(exibir_anuncios)
    form = FormAnuncio(instance=anuncio)
    context = {
        'form': form,
        'anuncio': anuncio
    }
    return render(request, 'editar_anuncio.html', context)

@login_required(login_url='/logar/')
def excluir_anuncio(request, id_anuncio):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    if anuncio.usuario != request.user:
        return redirect(exibir_anuncios)
    anuncio.delete()

    return redirect(exibir_anuncios)

def pagina_anuncio(request, id_anuncio):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    context = {
        'anuncio': anuncio,
        'vacinas': vacinas_anuncios.objects.filter(anuncio=anuncio)
    }
    return render(request, 'pagina_anuncio.html', context)

@login_required(login_url='/logar/')
def vacina_anuncio(request, id_anuncio):
    anuncio = Anuncio.objects.get(id=id_anuncio)
    if request.method == 'POST':
        form = FormVacinaAnuncio(request.POST)
        if form.is_valid():
            salvamento = form.save(commit=False)
            salvamento.anuncio = anuncio
            salvamento.save()
    form = FormVacinaAnuncio()
    context = {
        'anuncio': anuncio,
        'form': form,
    }
    return render(request, 'vacina_anuncio.html', context)

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect(exibir_anuncios)
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'logar_deslogar.html', context)


def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(logar)
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'logar_deslogar.html', context)

def deslogar(request):
    logout(request)

    return redirect(logar)

def anuncios_pessoais(request):
    anuncios = Anuncio.objects.filter(usuario=request.user)
    context = {
        'anuncios': anuncios
    }
    return render(request, 'anuncios_pessoais.html', context)