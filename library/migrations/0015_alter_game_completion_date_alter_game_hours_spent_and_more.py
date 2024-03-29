# Generated by Django 5.0 on 2024-02-28 18:05

import colorfield.fields
import django.core.validators
import django.db.models.deletion
import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_wishlistgame_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='completion_date',
            field=models.DateField(blank=True, default=django.db.models.functions.datetime.Now, help_text='Enter the date in the format YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='hours_spent',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='metacritic_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(help_text='Make sure you added at lest one platform before adding a game', on_delete=django.db.models.deletion.CASCADE, related_name='games', to='library.platform'),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True, help_text='Enter the date in the format YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='user_score',
            field=models.IntegerField(blank=True, help_text='Enter a number between 0 and 100', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='platform',
            name='background_color',
            field=colorfield.fields.ColorField(blank=True, default=None, help_text='Enter hex code to set the background color of the platform. If left blank, the black color will be used', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='platform',
            name='disk_size',
            field=models.IntegerField(blank=True, help_text='Enter the size in GB', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='platform',
            name='font_color',
            field=colorfield.fields.ColorField(blank=True, default='#fafafa', help_text='Enter hex code to set the font color for the platform. If left blank, the white color will be used', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='platform',
            name='ram',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='platform',
            name='subscription_fee',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter the cost per month', max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='wishlistgame',
            name='link',
            field=models.URLField(blank=True, help_text='Enter the url of the game you want to buy', null=True),
        ),
        migrations.AlterField(
            model_name='wishlistgame',
            name='platform',
            field=models.ForeignKey(help_text='Make sure you added at lest one platform before adding a game to the wishlist.', on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_games', to='library.platform'),
        ),
        migrations.AlterField(
            model_name='wishlistgame',
            name='priority',
            field=models.IntegerField(blank=True, help_text='Enter a value between 1 and 10 the The lower the number, the higher the priority', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='wishlistgame',
            name='release_date',
            field=models.DateField(blank=True, help_text='Enter the date in the format YYYY-MM-DD', null=True),
        ),
    ]
