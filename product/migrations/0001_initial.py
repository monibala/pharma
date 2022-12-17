# Generated by Django 4.0.5 on 2022-12-06 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('rating', models.IntegerField(choices=[(5, '*****'), (4, '****'), (3, '***'), (2, '**'), (1, '*')], default=1)),
                ('slug', models.SlugField(blank=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('mrp', models.IntegerField(default=1)),
                ('offer_price', models.IntegerField(default=1)),
                ('offer_percentage', models.IntegerField(default=1)),
                ('image', models.ImageField(null='True', upload_to='media/')),
                ('slug', models.SlugField(blank=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
                ('subcategory_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='category.subcategory')),
                ('subsubcategory_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subsubcategory', to='category.subsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('apartmentname', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(default=1)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunchal Pradesh', 'Arunchal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Chattishgarh', 'Chattishgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Madhya Pradesh', 'Madhya Pradesh'), ('punjab', 'punjab'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('West Bengal', 'West Bengal')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
