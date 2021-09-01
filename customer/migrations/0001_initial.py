# Generated by Django 3.2.5 on 2021-08-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('worth', models.IntegerField()),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerWalletRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('is_used', models.IntegerField(default=0)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('flag', models.IntegerField(default=1)),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.adminuser')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branch.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.voucher')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('all_worth', models.IntegerField(default=0)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('flag', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.voucher')),
            ],
        ),
    ]
