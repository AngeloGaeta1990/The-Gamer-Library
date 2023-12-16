# Generated by Django 5.0 on 2023-12-16 18:47

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=255)),
                ('user_score', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('metacritic_score', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('game_image', models.BinaryField(null=True)),
                ('user_review', models.TextField(null=True)),
                ('genres', models.CharField(max_length=255, null=True)),
                ('release_date', models.DateField(null=True)),
                ('completion_date', models.DateField(auto_now_add=True, null=True)),
                ('developer', models.CharField(max_length=255, null=True)),
                ('platform', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('friends', models.ManyToManyField(related_name='user_friends', through='library.FriendList', to='library.userprofile')),
                ('games', models.ManyToManyField(to='library.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='played_games', to='library.userprofile'),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.userprofile'),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship', to='library.userprofile'),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=255)),
                ('game_image', models.BinaryField(null=True)),
                ('genres', models.CharField(max_length=255, null=True)),
                ('stores', models.CharField(max_length=255, null=True)),
                ('release_date', models.DateField(null=True)),
                ('platform', models.CharField(max_length=255, null=True)),
                ('developer', models.CharField(max_length=255, null=True)),
                ('players', models.ManyToManyField(blank=True, default=None, null=True, related_name='wishlisted_games', to='library.userprofile')),
            ],
            options={
                'unique_together': {('game_name', 'platform')},
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(to='library.wishlist'),
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('game_name', 'platform')},
        ),
        migrations.AlterUniqueTogether(
            name='friendlist',
            unique_together={('user', 'friend')},
        ),
    ]
