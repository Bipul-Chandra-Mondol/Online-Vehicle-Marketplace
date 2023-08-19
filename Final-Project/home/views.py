from django.shortcuts import render
from items.models import Product


from .utils import paginationProject

# Create your views here.


def home(request):
    product = Product.objects.all()
    custom_range, products = paginationProject(request, product, 2)
    return render(request, 'index.html', context={'products': products, 'custom_range': custom_range})


def contactPage(request):
    return render(request, 'contact.html')

# search functionality
from django.db.models import Q
def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(mode_name__icontains=query)| Q(description__icontains=query))
    return render(request, 'search_result.html', {'products': products})