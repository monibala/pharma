# Generated by Django 4.0.5 on 2023-03-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
