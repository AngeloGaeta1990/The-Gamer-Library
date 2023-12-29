# Generated by Django 5.0 on 2023-12-28 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_rename_game_image_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/game_images'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/platform_images'),
        ),
    ]
