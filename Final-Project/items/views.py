from django.shortcuts import render, get_object_or_404
from items.models import Product
from category.models import Category
# Create your views here.


def product_view(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()
        # print(products)
        specific_category = get_object_or_404(Category, slug=category_slug)
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    return render(request, 'store.html', context={'products': products, 'product_count': product_count, 'specific_category': specific_category})


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product_detail.html', context={'single_product': single_product})




