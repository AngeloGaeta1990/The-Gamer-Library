# Generated by Django 5.0 on 2024-01-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_platform_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='number',
        ),
    ]