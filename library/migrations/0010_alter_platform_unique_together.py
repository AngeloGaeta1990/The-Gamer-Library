# Generated by Django 5.0 on 2024-01-23 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_platform_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='platform',
            unique_together=set(),
        ),
    ]
