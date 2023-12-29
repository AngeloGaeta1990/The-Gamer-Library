# Generated by Django 5.0 on 2023-12-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_platform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='library/game_images'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='game_image',
            field=models.ImageField(blank=True, null=True, upload_to='library/wishlist_images'),
        ),
    ]
