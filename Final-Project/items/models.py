from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    mode_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    engine = models.CharField(max_length=200,blank=True)
    mpg = models.CharField(max_length=200,blank=True)

    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(
        upload_to="products/", default="933_ps.jpg", blank=True, null=True)
    images2 = models.ImageField(
        upload_to="products/", default="933_ps.jpg", blank=True, null=True)
    images3 = models.ImageField(
        upload_to="products/", default="933_ps.jpg", blank=True, null=True)
    images4 = models.ImageField(
        upload_to="products/", default="933_ps.jpg", blank=True, null=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.mode_name
