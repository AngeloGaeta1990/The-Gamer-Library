import uuid
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True, blank=True,
                                     validators=[MaxValueValidator(100)])
    metacritic_score = models.IntegerField(null=True, blank=True,
                                           validators=[MaxValueValidator(100)])
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    user_review = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True,
                                       default=models.functions.Now,
                                       )
    hours_spent = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True, blank=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE,
                                 related_name='games')

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
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WishListGame(models.Model):

    CURRENCIES = [
        ('£', '£'),
        ('$', '$',),
        ('€', '€', )
    ]

    STORES = [
        ("Steam", "Steam"),
        ("Epic", "Epic"),
        ("Playstation Store", "Playstation Store"),
        ("Xbox ", "Xbox"),
        ("Nintendo eshop", "Nintendo eshop")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    genres = models.CharField(max_length=255, null=True, blank=True)
    store = models.CharField(max_length=255, null=True, blank=True,
                             choices=STORES)
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True,  blank=True)
    priority = models.IntegerField(null=True, blank=True,)
    currency = models.CharField(max_length=2, null=True, blank=True,
                                choices=CURRENCIES)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True,
                               blank=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE,
                                 related_name='wishlist_games')

    class Meta:
        unique_together = ('name', 'platform')
        ordering = ["-priority"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate or set the UUID when the instance is first created
        if not self.id:
            self.id = uuid.uuid4()

        # Generate or set the slug only if it's not already set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Platform(models.Model):

    PLATFORM_CHOICES = [
        ('console', 'Console'),
        ('pc', 'PC'),
        ('service', 'Service'),
        ('mobile', 'Mobile')
    ]

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

    OPERATIVE_MOBILE_SYSTEMS_CHOICES = [
        ('iOS', 'iOS'),
        ('Android', 'Android')
    ]

    CURRENCIES = [
        ('£', '£'),
        ('$', '$',),
        ('€', '€', )
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,)
    category = models.CharField(max_length=10, choices=PLATFORM_CHOICES,
                                null=False, blank=False)
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    box_color = ColorField(null=True, blank=True)
    font_color = ColorField(null=True, blank=True, default='#fafafa')
    # PC exclusive
    operative_systems = models.CharField(max_length=50,
                                         choices=OPERATIVE_SYSTEMS_CHOICES,
                                         null=True, blank=True)
    gpu = models.CharField(max_length=255, null=True, blank=True)
    cpu = models.CharField(max_length=255, null=True, blank=True)
    ram = models.IntegerField(null=True, blank=True)
    disk_size = models.IntegerField(null=True, blank=True)
    disk_type = models.CharField(max_length=10, choices=DISK_TYPE_CHOICES,
                                 null=True, blank=True)
    # Console exclusive
    model = models.CharField(max_length=255, null=True,  blank=True)
    # Service exclusive
    currency = models.CharField(max_length=2, null=True, blank=True,
                                choices=CURRENCIES)
    subscription_fee = models.DecimalField(max_digits=5, decimal_places=2,
                                           null=True,  blank=True)
    plan = models.CharField(max_length=255, null=True,  blank=True)
    # Mobile exclusive
    brand = models.CharField(max_length=255, null=True,  blank=True)
    operative_systems = models.CharField(max_length=50,
                                         choices=OPERATIVE_SYSTEMS_CHOICES,
                                         null=True,  blank=True)
    # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='platform')

    class Meta:
        unique_together = ('name', 'user')
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate or set the UUID when the instance is first created
        if not self.id:
            self.id = uuid.uuid4()
        # Generate or set the slug only if it's not already set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def ordered_games(self):
        return self.games.all().order_by("name")
