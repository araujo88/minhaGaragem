from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Veiculo
from .forms import VeiculoForm
from django.contrib import messages
from .utils import searchVeiculos, paginateVeiculos

@login_required(login_url="/login/")
def veiculos(request):
    veiculos, search_query = searchVeiculos(request)
    custom_range, veiculos = paginateVeiculos(request, veiculos, 4)
    context = {'veiculos': veiculos, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'garagem/veiculos.html', context)

@login_required(login_url="/login/")
def veiculo(request, pk):
    veiculoObj = Veiculo.objects.get(id=pk)
    print('veiculoObj:', veiculoObj)
    context = {'veiculo': veiculoObj}
    return render(request, 'garagem/veiculos.html', context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="login")
def criarVeiculo(request):
    form = VeiculoForm(user=request.user)

    if request.method == 'POST':
        form = VeiculoForm(user=request.user, data=request.POST)
        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.user = request.user
            veiculo.save()
            messages.success(request, 'O veículo foi adicionado com sucesso!')
            return redirect('veiculos')

    context = {'form': form}
    return render(request, "garagem/veiculo_form.html", context)

@login_required(login_url="login")
def editarVeiculo(request, pk):
    veiculo = Veiculo.objects.get(id=pk)
    form = VeiculoForm(user=request.user, instance=veiculo)

    if request.method == 'POST':
        form = VeiculoForm(user=request.user, data=request.POST, instance=veiculo)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('veiculos')

    context = {'form': form}
    return render(request, "garagem/veiculo_form.html", context)

@login_required(login_url="login")
def deletarVeiculo(request, pk):
    veiculo = Veiculo.objects.get(id=pk)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculos')

    context = {'object': veiculo}
    return render(request, 'garagem/delete_template.html', context)