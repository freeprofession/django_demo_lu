from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class RoleHasPermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    permission = models.ForeignKey(Permission, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class AdminUser(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tel = models.CharField(max_length=225)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_login = models.IntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_available = models.IntegerField(default=1)
    flag = models.IntegerField(default=1)


class AdminUserHasRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=1)


class AdminUserRecord(models.Model):
    admin_user = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=255)
    msg = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
