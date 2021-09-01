from django.db import models
from goods.models import Goods, GoodsDiscount, GoodsHasSku
from admin_user.models import AdminUser


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    foreman = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class BranchHasGoods(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    goods_sku = models.ForeignKey(GoodsHasSku, on_delete=models.DO_NOTHING)
    discount = models.ForeignKey(GoodsDiscount, on_delete=models.DO_NOTHING, blank=True, null=True)
    inventory = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class BranchHasAdminUser(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)

