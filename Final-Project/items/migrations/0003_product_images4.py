# Generated by Django 4.1.7 on 2023-03-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_product_images2_product_images3_alter_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images4',
            field=models.ImageField(blank=True, default='933_ps.jpg', null=True, upload_to='products/'),
        ),
    ]