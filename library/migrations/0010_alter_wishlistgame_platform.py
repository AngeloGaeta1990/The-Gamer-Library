# Generated by Django 5.0 on 2024-02-08 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_wishlistgame_delete_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistgame',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_games', to='library.platform'),
        ),
    ]
