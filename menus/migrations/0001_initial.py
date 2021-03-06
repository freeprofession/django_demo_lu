# Generated by Django 3.2.5 on 2021-08-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('page_url', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('before_menu_id', models.IntegerField()),
                ('show', models.IntegerField(default=1)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RoleHasMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menus.menu')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.role')),
            ],
        ),
    ]
