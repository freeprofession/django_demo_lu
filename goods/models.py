from django.db import models
import uuid


class GoodsBrand(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class GoodsCategory(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField(default=1)
    pic_url = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class GoodsImage(models.Model):
    pic_url = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class Goods(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(GoodsBrand, on_delete=models.DO_NOTHING)
    sale_price = models.IntegerField()
    pic_url = models.CharField(max_length=255, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)
    describe = models.TextField(blank=True, null=True)


class CategoryHasGoods(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class GoodsSku(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class GoodsHasSku(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    sku = models.ForeignKey(GoodsSku, on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=255)
    pic_url = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class GoodsDiscount(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class GoodsHasImage(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(GoodsImage, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)
