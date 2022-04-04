from django.db import models

from users.models import User
from cores.timestamp import TimeStamp

class Product(TimeStamp):
    name        = models.CharField(max_length=45)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    size        = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    howtouse    = models.JSONField()
    badge       = models.CharField(max_length=15, null=True)
    skin_type   = models.ManyToManyField('SkinType', through='ProductSkintype')

    
    class Meta:
        db_table = 'products'

class Feeling(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'feelings'

class ProductFeelings(models.Model):
    product = models.ForeignKey('Product' , on_delete=models.CASCADE )
    feeling = models.ForeignKey('Feeling' , on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_feelings'

class Category(models.Model):
    category_name = models.CharField(max_length=45)
    main_description = models.CharField(max_length=1000, null=True)
    sub_description = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'categories'

class Ingredient(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'ingredients'

class ProductIngredient(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    major       = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_ingredients'

class ProductImage(models.Model):
    url = models.CharField(max_length=2000, null=True)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_imgaes'
    
class SkinType(models.Model):
    name = models.CharField(max_length=45)
    
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