# Generated by Django 5.0 on 2024-02-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_alter_game_user_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistgame',
            name='link',
            field=models.URLField(blank=True, help_text='Enter the url of the game you want to buy.', null=True),
        ),
    ]