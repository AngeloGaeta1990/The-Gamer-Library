# Generated by Django 5.0 on 2024-02-07 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_wishlist_options_wishlist_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='stores',
            new_name='store',
        ),
    ]
