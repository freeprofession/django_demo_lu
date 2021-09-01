from django.db import models
from admin_user.models import AdminUser
from branch.models import Branch
from goods.models import GoodsHasSku
from customer.models import Customer
from supplier.models import Supplier
import uuid


class SaleOrder(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    goods_sku = models.ForeignKey(GoodsHasSku, on_delete=models.DO_NOTHING)
    number = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    sale_price = models.IntegerField()
    state = models.IntegerField(default=0)
    is_deal = models.IntegerField(default=0)
    node = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class SaleOrderRecord(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.DO_NOTHING)
    type = models.IntegerField(default=0)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class PurchaseOrder(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1)
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    fee = models.FloatField()
    all_num = models.IntegerField()
    all_price = models.FloatField()
    real_price = models.FloatField()
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    state = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    goods_sku = models.ForeignKey(GoodsHasSku, on_delete=models.DO_NOTHING)
    purchase_number = models.IntegerField()
    get_number = models.IntegerField(blank=True, null=True)
    purchase_price = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class PurchaseOrderRecord(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    type = models.IntegerField(default=0)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class UndonePurchaseOrder(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    goods_sku = models.ForeignKey(GoodsHasSku, on_delete=models.DO_NOTHING)
    type = models.IntegerField(default=0)
    number = models.IntegerField()
    purchase_price = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)
