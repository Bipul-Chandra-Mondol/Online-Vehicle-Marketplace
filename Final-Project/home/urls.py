
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('contact/', views.contactPage, name="contact"),
    path('search_result/',views.search_products,name='search_product'),
]
