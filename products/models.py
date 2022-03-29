from django.db import models

from users.models import User
from cores.timestamp import TimeStamp

# Create your models here.
class Product(TimeStamp):
    name        = models.CharField(max_length=45)
    price       = models.CharField(max_length=45)
    size        = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    feeling     = models.CharField(max_length=45)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    howtouse    = models.JSONField()
    
    class Meta:
        db_table = 'products'

class Category(models.Model):
    category_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Ingredient(models.Model):
    ingredients = models.CharField(max_length=300)

    class Meta:
        db_table = 'ingredients'

class ProductIngredient(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    squence    = models.IntegerField()

    class Meta:
        db_table = 'product_ingredients'

class ProductImage(models.Model):
    image_url = models.CharField(max_length=200)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_imgaes'
    
class SkinType(models.Model):
    skin_type = models.CharField(max_length=45)

    class Meta:
        db_table = 'skin_types'

class ProductSkintype(models.Model):
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)
    skin_type = models.ForeignKey('SkinType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_skintypes'


class Review(TimeStamp):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey('Product' , on_delete=models.CASCADE, related_name='products')
    content = models.CharField(max_length=400)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    review    = models.ForeignKey('Review' , on_delete=models.CASCADE , related_name='reviews')
    image_url = models.CharField(max_length=300)

    class Meta:
        db_table = 'review_images'