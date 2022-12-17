# Generated by Django 4.0.5 on 2022-12-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_brands'),
        ('order', '0011_orderitem_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='cartitem',
            field=models.ManyToManyField(to='product.cart', verbose_name='cart'),
        ),
    ]
