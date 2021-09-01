from django.db import models
from admin_user.models import AdminUser
from branch.models import Branch


class Customer(models.Model):
    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    tel = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class Voucher(models.Model):
    name = models.CharField(max_length=255)
    worth = models.IntegerField()
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class CustomerWallet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    voucher = models.ForeignKey(Voucher, on_delete=models.DO_NOTHING)
    number = models.IntegerField(default=0)
    all_worth = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)


class CustomerWalletRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    voucher = models.ForeignKey(Voucher, on_delete=models.DO_NOTHING)
    value = models.IntegerField()
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    is_used = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)
