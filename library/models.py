import uuid
from django.db import models
from django.core.validators import MaxValueValidator
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings



# class CustomUser(AbstractUser):
#     # Add your custom fields here
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


#     def __str__(self):
#         return self.username



class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True,  blank=True, validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField( null=True,  blank=True, validators=[MaxValueValidator(100)])
    image = models.ImageField(upload_to='library/game_images', null=True,  blank=True)
    user_review = models.TextField(null=True,  blank=True)
    genres = models.CharField(max_length=255,  blank=True, null=True)
    release_date = models.DateField(null=True,  blank=True)
    completion_date = models.DateField(null=True, auto_now_add=True,  blank=True)
    hours_spent = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    platform = models.ForeignKey('Platform', on_delete=models.SET_NULL, blank=True, null=True, related_name='games')
    

    class Meta:
        unique_together = ('name', 'platform')
        ordering = ["platform"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate or set the UUID when the instance is first created
        if not self.id:
            self.id = uuid.uuid4()

        # Generate or set the slug only if it's not already set
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')

        super().save(*args, **kwargs)



class WishList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    game_name = models.CharField(max_length=255)
    game_image = models.ImageField( upload_to='library/wishlist_images', null=True,  blank=True)
    game_genres = models.CharField(max_length=255, null=True,  blank=True)
    stores = models.CharField(max_length=255, null=True,  blank=True)
    release_date = models.DateField(null=True,  blank=True)
    game_platform = models.ForeignKey('Platform',  on_delete=models.SET_NULL, blank=True, null=True, related_name='wishlists')
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
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=10, choices=PLATFORM_CHOICES, null=False, blank=False)
    image = models.ImageField( upload_to='library/platform_images', null=True, blank=True)
    box_color = ColorField(null=True,  blank=True)
    font_color = ColorField(null=True,  blank=True, default='#fafafa')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='platform')
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate or set the UUID when the instance is first created
        if not self.id:
            self.id = uuid.uuid4()

        # Generate or set the slug only if it's not already set
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')

        super().save(*args, **kwargs)

class PCPlatform(Platform):
    OPERATIVE_SYSTEMS_CHOICES = [
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('MacOS', 'MacOS'),
        ('Android', 'Android')
    ]

    DISK_TYPE_CHOICES = [
        ('HDD', 'HDD'),
        ('SSD', 'SSD')
    ]
    operative_systems = models.CharField(max_length=50, choices=OPERATIVE_SYSTEMS_CHOICES)
    gpu = models.CharField(max_length=255, null=True,  blank=True)
    cpu = models.CharField(max_length=255, null=True,  blank=True)
    ram = models.IntegerField(null=True, blank=True)
    disk_size = models.IntegerField(null=True, blank=True)
    disk_type =  models.CharField(max_length=10, choices= DISK_TYPE_CHOICES, null=True, blank=True)



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