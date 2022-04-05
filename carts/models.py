from django.db import models

from products.models import Product
from users.models import User
from cores.timestamp import TimeStamp


class Cart(TimeStamp):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'carts'