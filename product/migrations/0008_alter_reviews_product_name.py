# Generated by Django 4.0.5 on 2022-12-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_reviews_product_name_reviews_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='product_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
