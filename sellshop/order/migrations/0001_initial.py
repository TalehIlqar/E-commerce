# Generated by Django 3.2.7 on 2021-11-17 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_remove_productversion_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_ordered', models.BooleanField(default=False, verbose_name='Is Ordered?')),
                ('ordered_at', models.DateTimeField(blank=True, null=True, verbose_name='Ordered at')),
                ('product', models.ManyToManyField(blank=True, to='product.ProductVersion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=255, verbose_name='City')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', django_countries.fields.CountryField(max_length=255, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(blank=True, related_name='Product_wishlist', to='product.ProductVersion')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(blank=True, help_text='Max 255 char.', max_length=255, null=True, verbose_name='Company name')),
                ('address', models.TextField(verbose_name='Address')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_City', to='order.city', verbose_name='City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_Country', to='order.country', verbose_name='Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Shipping', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City_Country', to='order.country', verbose_name='Country'),
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Cart', to='order.cart')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productversion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='shipping_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.shippingaddress', verbose_name='Shipping Address'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(help_text='Max 255 char.', max_length=255, verbose_name='Company name')),
                ('address', models.TextField(verbose_name='Address')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Billing_City', to='order.city', verbose_name='City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Billing_Country', to='order.country', verbose_name='Country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User_Billing', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
