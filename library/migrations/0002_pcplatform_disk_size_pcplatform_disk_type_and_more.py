# Generated by Django 5.0 on 2023-12-25 23:18

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcplatform',
            name='disk_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pcplatform',
            name='disk_type',
            field=models.CharField(blank=True, choices=[('HDD', 'HDD'), ('SSD', 'SSD')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=None),
        ),
    ]