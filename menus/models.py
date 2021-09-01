from django.db import models
from admin_user.models import Role, Permission


class Menu(models.Model):
    name = models.CharField(max_length=255)
    page_url = models.CharField(max_length=255)
    page_name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    before_menu_id = models.IntegerField(blank=True, null=True)
    show = models.IntegerField(default=1)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class RoleHasMenu(models.Model):
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class MenuHasPermission(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    permission = models.ForeignKey(Permission, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)
