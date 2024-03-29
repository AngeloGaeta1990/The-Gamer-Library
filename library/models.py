import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from colorfield.fields import ColorField


class Game(models.Model):
    """
    Model for games. It has a many to one relationship with the Platform model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    user_score = models.IntegerField(null=True, blank=True,
                                     validators=[MinValueValidator(0),
                                                 MaxValueValidator(100)],
                                     help_text='Enter a number between 0 and'
                                               ' 100')
    metacritic_score = models.IntegerField(null=True, blank=True,
                                           validators=[MinValueValidator(0),
                                                       MaxValueValidator(100)])
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    user_review = models.TextField(max_length=2000, null=True, blank=True)
    genres = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True,
                                    help_text='Enter the date in the format'
                                    ' YYYY-MM-DD')
    completion_date = models.DateField(null=True, blank=True,
                                       default=models.functions.Now,
                                       help_text='Enter the date in the format'
                                       ' YYYY-MM-DD')
    hours_spent = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(0)])
    developer = models.CharField(max_length=255, null=True, blank=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE,
                                 related_name='games',
                                 help_text='Make sure you added at lest one'
                                 ' platform before adding a game')

    class Meta:
        unique_together = ('name', 'platform')
        ordering = ['platform']

    @property
    def image_url(self):
        if self.image:
            return self.image.build_url(secure=True)
        return None

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WishListGame(models.Model):
    """
    Model for the wishlist games. It has a many to one relationship with the
    platform model.
    """

    CURRENCIES = [
        ('£', '£'),
        ('$', '$'),
        ('€', '€')
    ]

    STORES = [
        ('Steam', 'Steam'),
        ('Epic', 'Epic'),
        ('Playstation Store', 'Playstation Store'),
        ('Xbox', 'Xbox'),
        ('Nintendo eshop', 'Nintendo eshop')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    genres = models.CharField(max_length=255, null=True, blank=True)
    store = models.CharField(max_length=255, null=True, blank=True,
                             choices=STORES)
    release_date = models.DateField(null=True, blank=True, help_text='Enter'
                                    ' the date in the format YYYY-MM-DD')
    developer = models.CharField(max_length=255, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(10)],
                                   help_text='Enter a'
                                   ' value between 1 and 10 the'
                                   ' The lower the number, the higher the'
                                   ' priority')
    link = models.URLField(max_length=200, null=True, blank=True,
                           help_text='Enter the url of the game you want to'
                                     ' buy')
    currency = models.CharField(max_length=2, null=True, blank=True,
                                choices=CURRENCIES)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True,
                               blank=True, validators=[MinValueValidator(0)])
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE,
                                 related_name='wishlist_games',
                                 help_text='Make sure you added at lest one'
                                 ' platform before adding a game to the'
                                 ' wishlist.')

    class Meta:
        unique_together = ('name', 'platform')
        ordering = ['-priority']

    @property
    def image_url(self):
        if self.image:
            return self.image.build_url(secure=True)
        return None

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Platform(models.Model):
    """
    Model for the platforms. It has a many to one relationship with the User
    """

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
        ('$', '$'),
        ('€', '€')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=10, choices=PLATFORM_CHOICES,
                                null=False, blank=False)
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    background_color = ColorField(null=True, blank=True, help_text='Enter hex'
                                  ' code to set the background color of the'
                                  ' platform. If left blank, the black color'
                                  ' will be used')
    font_color = ColorField(null=True, blank=True, default='#fafafa',
                            help_text='Enter hex code to set the font color'
                            ' for the platform. If left blank,'
                            ' the white color will be used')
    operative_systems = models.CharField(max_length=50,
                                         choices=OPERATIVE_SYSTEMS_CHOICES,
                                         null=True, blank=True)
    gpu = models.CharField(max_length=255, null=True, blank=True)
    cpu = models.CharField(max_length=255, null=True, blank=True)
    ram = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(0), MaxValueValidator(100)])
    disk_size = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(0), MaxValueValidator(100)],
                                    help_text='Enter the size in GB')
    disk_type = models.CharField(max_length=10, choices=DISK_TYPE_CHOICES,
                                 null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=2, null=True, blank=True,
                                choices=CURRENCIES)
    subscription_fee = models.DecimalField(max_digits=5, decimal_places=2,
                                           null=True, blank=True,
                                           validators=[MinValueValidator(0)],
                                           help_text='Enter the cost per'
                                           ' month')
    plan = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    operative_systems = models.CharField(max_length=50,
                                         choices=OPERATIVE_SYSTEMS_CHOICES,
                                         null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='platform')

    class Meta:
        unique_together = ('name', 'user')
        ordering = ['name']

    @property
    def image_url(self):
        if self.image:
            return self.image.build_url(secure=True)
        return None

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def ordered_games(self):
        return self.games.all().order_by('name')
