# Generated by Django 5.0 on 2024-02-07 20:30

import cloudinary.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_rename_stores_wishlist_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListGame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image')),
                ('genres', models.CharField(blank=True, max_length=255, null=True)),
                ('store', models.CharField(blank=True, choices=[('Steam', 'Steam'), ('Epic', 'Epic'), ('Playstation Store', 'Playstation Store'), ('Xbox ', 'Xbox'), ('Nintendo eshop', 'Nintendo eshop')], max_length=255, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('developer', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, choices=[('£', '£'), ('$', '$'), ('€', '€')], max_length=2, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='library.platform')),
            ],
            options={
                'ordering': ['-priority'],
                'unique_together': {('name', 'platform')},
            },
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
