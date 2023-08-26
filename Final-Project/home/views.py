from django.shortcuts import render
from items.models import Product
from django.http import JsonResponse
from django.db.models import Q

from .utils import paginationProject

# Create your views here.


def home(request):
    product = Product.objects.all()
    custom_range, products = paginationProject(request, product, 2)
    return render(request, 'index.html', context={'products': products, 'custom_range': custom_range})


def contactPage(request):
    return render(request, 'contact.html')

# search functionality
# from django.db.models import Q
# def search_products(request):
#     query = request.GET.get('q')
#     products = Product.objects.filter(
#         Q(mode_name__icontains=query)| Q(description__icontains=query))
#     return render(request, 'search_result.html', {'products': products})

# auto search suggestion functioality
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(mode_name__icontains=query)[:5]
        suggestions = [{'mode_name': product.mode_name} for product in products]
    else:
        if "application/json" in request.META.get('HTTP_ACCEPT'):
            return JsonResponse([],safe=False)
        else:
            products=None
            return render(request, 'search_result.html', {'products': products})
    if "application/json" in request.META.get('HTTP_ACCEPT'):
        return JsonResponse(suggestions, safe=False)
    else:
        return render(request, 'search_result.html', {'products': products})

