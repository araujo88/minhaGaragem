from .models import Veiculo
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateVeiculos(request, veiculos, results):

    page = request.GET.get('page')
    paginator = Paginator(veiculos, results)

    try:
        veiculos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        veiculos = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        veiculos = paginator.page(page)
    
    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, veiculos

def searchVeiculos(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    veiculos = Veiculo.objects.distinct().filter(
        Q(tipo__icontains=search_query) | 
        Q(cor__icontains=search_query) | 
        Q(modelo__icontains=search_query) | 
        Q(ano__icontains=search_query)
    )

    if (request.user.is_superuser == False):
        veiculos = veiculos.filter(user = request.user)

    return veiculos, search_query