# Generated by Django 5.0 on 2024-01-23 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_game_slug_alter_platform_slug_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='platform',
            unique_together={('name',)},
        ),
    ]
