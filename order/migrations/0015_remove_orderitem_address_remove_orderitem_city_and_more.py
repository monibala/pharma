# Generated by Django 4.0.5 on 2022-12-15 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_remove_update_order_quntity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='zipcode',
        ),
    ]