from .models import Pessoa
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatePessoas(request, pessoas, results):

    page = request.GET.get('page')
    paginator = Paginator(pessoas, results)

    try:
        pessoas = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        pessoas = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        pessoas = paginator.page(page)
    
    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, pessoas

def searchPessoas(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    pessoas = Pessoa.objects.filter(
        Q(nome__icontains=search_query) |
        Q(documento__icontains=search_query) |
        Q(telefone__icontains=search_query) | 
        Q(email__icontains=search_query))

    if (request.user.is_superuser == False):
        pessoas = pessoas.filter(user = request.user)

    return pessoas, search_query