import uuid
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
# class CustomUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField(max_length = 255)
#     friends = models.ManyToManyField('self', through='FriendList', symmetrical=False, related_name='user_friends')
#     games = models.ForeignKey('Game',  on_delete=models.CASCADE, blank=True)
#     wishlists = models.ForeignKey('WishList',  on_delete=models.CASCADE, blank=True)
#     platforms = models.ForeignKey('Platform', on_delete=models.CASCADE, blank= True)

#     def __str__(self):
#         return self.username

    
class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True,  blank=True, validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField( null=True,  blank=True, validators=[MaxValueValidator(100)])
    game_image = models.ImageField(null=True,  blank=True)
    user_review = models.TextField(null=True,  blank=True)
    genres = models.CharField(max_length=255,  blank=True, null=True)
    release_date = models.DateField(null=True,  blank=True)
    completion_date = models.DateField(null=True, auto_now_add=True,  blank=True)
    hours_spent = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    platform = models.ForeignKey('Platform',  on_delete=models.SET_NULL, blank=True, null=True, )

    class Meta:
        unique_together = ('name', 'platform')
        ordering = ["platform"]

    def __str__(self):
        return self.game_name


class WishList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=255)
    game_image = models.ImageField(null=True,  blank=True)
    game_genres = models.CharField(max_length=255, null=True,  blank=True)
    stores = models.CharField(max_length=255, null=True,  blank=True)
    release_date = models.DateField(null=True,  blank=True)
    game_platform = models.ForeignKey('Platform',  on_delete=models.SET_NULL, blank=True, null=True, related_name='wishlists_platform')
    developer = models.CharField(max_length=255, null=True,  blank=True)

    class Meta:
        unique_together = ('game_name', 'game_platform')
        ordering = ["game_platform"]

    def __str__(self):
        return self.game_name

#TODO check if it possible to create PC, console and Service subclass
#TODO add plan and hardware specs
class Platform(models.Model):

    PLATFORM_CHOICES = [
        ('console', 'Console'),
        ('pc', 'PC'),
        ('service', 'Service'),
        ('mobile', 'Mobile')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=PLATFORM_CHOICES, null=False, blank=False)
    image = models.ImageField(null=True,  blank=True)
    games = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True, null=True, related_name='platform_games' )
    wishlists = models.ForeignKey('WishList', on_delete=models.CASCADE,  blank=True, null=True, related_name='platform_wish_list')
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class PCPlatform(Platform):
    OPERATIVE_SYSTEMS_CHOICES = [
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('MacOS', 'MacOS'),
        ('Android', 'Android')
    ]
    operative_systems = models.CharField(max_length=50, choices=OPERATIVE_SYSTEMS_CHOICES)
    gpu = models.CharField(max_length=255, null=True,  blank=True)
    cpu = models.CharField(max_length=255, null=True,  blank=True)
    ram = models.IntegerField(null=True, blank=True)
  


    
class ConsolePlatform(Platform):

    model = models.CharField(max_length=255, null=True,  blank=True)


class ServicePlatform(Platform):

    subscription_fee = models.DecimalField(max_digits=5, decimal_places=2,  null=True,  blank=True)
    plan = models.CharField(max_length=255, null=True,  blank=True)



class MobilePlatform(Platform):
    OPERATIVE_SYSTEMS_CHOICES = [
        ('OS', 'OS'),
        ('Android', 'Android')
    ]

    brand = models.CharField(max_length=255, null=True,  blank=True)
    operative_systems = models.CharField(max_length=50, choices=OPERATIVE_SYSTEMS_CHOICES)


# class FriendList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friendship', null=False )
#     friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)

#     class Meta:
#         unique_together = ('user', 'friend')