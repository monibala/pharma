# Generated by Django 4.0.5 on 2022-12-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('author', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
