# Generated by Django 4.0.5 on 2022-12-07 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_reviews_product_name_reviews_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='product_name',
        ),
        migrations.AddField(
            model_name='reviews',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
