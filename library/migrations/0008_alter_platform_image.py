# Generated by Django 5.0 on 2023-12-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_game_image_alter_platform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='platform_images'),
        ),
    ]
