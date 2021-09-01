from django.db import models
from goods.models import GoodsHasSku


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pay_detail = models.TextField()
    connection_detail = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class SupplierHasGoods(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    goods_sku = models.ForeignKey(GoodsHasSku, on_delete=models.DO_NOTHING)
    purchase_price = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)
