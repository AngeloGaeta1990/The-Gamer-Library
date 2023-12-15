from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True,  validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField( null=True,  validators=[MaxValueValidator(100)])
    game_image = models.BinaryField(null=True)
    user_review = models.TextField(null=True)
    genres = models.CharField(max_length=255, null=True)
    release_date = models.DateField(null=True)
    developer = models.CharField(max_length=255, null=True)
    platform = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ('game_name', 'platform')

class WishList(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_name = models.BinaryField()
    game_image = models.BinaryField(null=True)
    genres = models.CharField(max_length=255, null=True)
    stores = models.CharField(max_length=255, null=True)
    release_date = models.DateField(null=True)
    platform = models.CharField(max_length=255, null=True)
    developer = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ('game_name', 'platform')

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('user', 'game')



class UserWishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(WishList, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('user', 'game')

class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE)