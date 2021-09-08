from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PessoaForm
from django.contrib import messages
from .utils import searchPessoas, paginatePessoas

# Create your views here.

@login_required(login_url="/login/") 
def pessoas(request):
    pessoas, search_query = searchPessoas(request)
    custom_range, pessoas = paginatePessoas(request, pessoas, 4)
    context = {'pessoas': pessoas, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'pessoa/usuarios.html', context)

@login_required(login_url="/login/")
def pessoa(request, pk):
    pessoaObj = Pessoa.objects.get(id=pk)
    print('veiculoObj:', pessoaObj)
    return render(request, 'pessoa/usuarios.html', {'pessoa': pessoaObj})

@login_required(login_url="login")
def criarUsuario(request):
    form = PessoaForm()

    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.user = request.user
            pessoa.save()
            messages.success(request, 'O usuário foi adicionado com sucesso!')
            return redirect('pessoas')

    context = {'form': form}
    return render(request, "pessoa/pessoa_form.html", context)

@login_required(login_url="login")
def editarUsuario(request, pk):
    pessoa = Pessoa.objects.get(id=pk)
    form = PessoaForm(instance=pessoa)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('pessoas')

    context = {'form': form}
    return render(request, "pessoa/pessoa_form.html", context)

@login_required(login_url="login")
def deletarUsuario(request, pk):
    pessoa = Pessoa.objects.get(id=pk)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoas')

    context = {'object': pessoa}
    return render(request, 'pessoa/delete_template.html', context)