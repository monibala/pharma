# Generated by Django 4.0.5 on 2023-03-17 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_subsubcategory_name'),
        ('product', '0011_product_availability_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory_name',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='category.subcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subsubcategory_name',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='subsubcategory', to='category.subsubcategory'),
        ),
    ]