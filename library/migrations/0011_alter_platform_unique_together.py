# Generated by Django 5.0 on 2024-01-23 20:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_platform_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='platform',
            unique_together={('name', 'user')},
        ),
    ]
