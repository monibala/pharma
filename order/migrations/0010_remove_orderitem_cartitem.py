# Generated by Django 4.0.5 on 2022-12-14 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_orderitem_address_orderitem_city_orderitem_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cartitem',
        ),
    ]