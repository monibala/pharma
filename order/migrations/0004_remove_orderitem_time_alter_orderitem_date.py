# Generated by Django 4.0.5 on 2023-03-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderitem_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='time',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
