# Generated by Django 4.0.5 on 2022-12-06 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='product_pyment_id')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('zipcode', models.IntegerField(default=1)),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('quntity', models.IntegerField(default=1)),
                ('payment', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wishitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='update_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updt_id', models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='updt_pyment_id')),
                ('updt_date', models.DateTimeField(auto_now_add=True)),
                ('prod_orders', models.ManyToManyField(to='order.orderitem', verbose_name='product_order')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
