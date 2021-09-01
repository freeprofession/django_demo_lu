# Generated by Django 3.2.5 on 2021-08-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=225)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('is_login', models.IntegerField(default=0)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RoleHasPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.role')),
            ],
        ),
        migrations.CreateModel(
            name='AdminUserHasRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.adminuser')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.role')),
            ],
        ),
    ]