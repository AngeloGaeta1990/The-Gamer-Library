# Generated by Django 5.0 on 2024-01-23 21:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_platform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='image/upload/default_platform_ipx1nh', max_length=255, null=True, verbose_name='image'),
        ),
    ]
