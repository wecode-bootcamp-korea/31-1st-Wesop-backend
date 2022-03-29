from django.db import models

from products.models import Product
from users.models    import User
from cores.timestamp import TimeStamp

class Order(TimeStamp):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    detail          = models.CharField(max_length=400)
    order_status    = models.ForeignKey('OrderStatus')

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_status'

class OrderItem(models.Model):
    product            = models.ForeignKey(Product , on_delete=models.CASCADE)
    order              = models.ForeignKey('Order' , on_delete=models.CASCADE)
    oreder_item_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    quantity           = models.IntegerField()
    total_price        = models.IntegerField()

    class Meta:
        db_table = 'order_items'

class OrderItemStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_item_status'

class Shipment(TimeStamp):
    order        = models.ForeignKey('Order', on_delete=models.CASCADE)
    tracking_num = models.IntegerField()

    class Meta:
        db_table = 'shipments'