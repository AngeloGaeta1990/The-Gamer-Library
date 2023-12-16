import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    friends = models.ManyToManyField('self', through='FriendList', symmetrical=False, related_name='user_friends')
    games = models.ManyToManyField('Game', blank=True)
    wishlist = models.ManyToManyField('WishList', blank=True)

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True,  blank=True, validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField( null=True,  blank=True, validators=[MaxValueValidator(100)])
    game_image = models.BinaryField(null=True,  blank=True)
    user_review = models.TextField(null=True,  blank=True)
    genres = models.CharField(max_length=255,  blank=True, null=True)
    release_date = models.DateField(null=True,  blank=True)
    completion_date = models.DateField(null=True, auto_now_add=True,  blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    platform = models.CharField(max_length=255, null=True,  blank=True)
    players = models.ManyToManyField('UserProfile', related_name='played_games', blank=True, null=True, default=None)

    class Meta:
        unique_together = ('game_name', 'platform')


class WishList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=255)
    game_image = models.BinaryField(null=True,  blank=True)
    genres = models.CharField(max_length=255, null=True,  blank=True)
    stores = models.CharField(max_length=255, null=True,  blank=True)
    release_date = models.DateField(null=True,  blank=True)
    platform = models.CharField(max_length=255, null=True,  blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    players = models.ManyToManyField('UserProfile', related_name='wishlisted_games', blank=True, null=True, default=None)

    class Meta:
        unique_together = ('game_name', 'platform')


class FriendList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friendship', null=False )
    friend = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('user', 'friend')