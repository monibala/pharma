# Generated by Django 4.0.5 on 2023-03-31 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_update_order_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_order',
            name='amount',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 12, 26, 55, 138151)),
        ),
    ]