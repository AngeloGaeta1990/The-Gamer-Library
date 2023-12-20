import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    friends = models.ManyToManyField('self', through='FriendList', symmetrical=False, related_name='user_friends')
    games = models.ForeignKey('Game',  on_delete=models.CASCADE, blank=True)
    wishlists = models.ForeignKey('WishList',  on_delete=models.CASCADE, blank=True)
    platforms = models.ForeignKey('Platform', on_delete=models.CASCADE, blank= True)

    def __str__(self):
        return self.username


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True,  blank=True, validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField( null=True,  blank=True, validators=[MaxValueValidator(100)])
    game_image = models.ImageField(null=True,  blank=True)
    user_review = models.TextField(null=True,  blank=True)
    genres = models.CharField(max_length=255,  blank=True, null=True)
    release_date = models.DateField(null=True,  blank=True)
    completion_date = models.DateField(null=True, auto_now_add=True,  blank=True)
    hours_spent = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    platform = models.CharField(max_length=255, null=True,  blank=True)

    class Meta:
        unique_together = ('game_name', 'platform')
        ordering = ["platform"]

    def __str__(self):
        return self.game_name


class WishList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=255)
    game_image = models.ImageField(null=True,  blank=True)
    genres = models.CharField(max_length=255, null=True,  blank=True)
    stores = models.CharField(max_length=255, null=True,  blank=True)
    release_date = models.DateField(null=True,  blank=True)
    platform = models.CharField(max_length=255, null=True,  blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)

    class Meta:
        unique_together = ('game_name', 'platform')
        ordering = ["platform"]

    def __str__(self):
        return self.game_name

#TODO check if it possible to create PC, console and Service subclass
#TODO add plan and hardware specs
class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform_name = models.CharField(max_length=255)
    platform_image = models.ImageField(null=True,  blank=True)
    platform_model = models.CharField(max_length=255, null=True,  blank=True)
    games = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True, null=True, related_name='games' )
    wishlists = models.ForeignKey('WishList', on_delete=models.CASCADE,  blank=True, null=True, related_name='wish_list')

    ordering = ["platform_name"]

    def __str__(self):
        return self.platform_name

class FriendList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friendship', null=False )
    friend = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('user', 'friend')