# Generated by Django 4.0.5 on 2022-12-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_update_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_order',
            name='product',
            field=models.ManyToManyField(to='order.orderitem'),
        ),
    ]
