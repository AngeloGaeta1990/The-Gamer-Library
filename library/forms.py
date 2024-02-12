from django.core.validators import FileExtensionValidator, MaxValueValidator
from django import forms
from .models import Platform, Game, WishListGame


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image')

    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                           'jpeg', 'webp', 'gif']),
                    MaxValueValidator(limit_value=1024 * 1024 * 50)])


class EditPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image', 'box_color', 'font_color')


class EditPCPlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('operative_systems', 'gpu',
                                                 'cpu', 'ram', 'disk_size',
                                                 'disk_type')


class EditConsolePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('model',)


class EditServicePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('currency',
                                                 'subscription_fee',
                                                 'plan')


class EditMobilePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('brand', 'operative_systems')


class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'platform', 'image', 'user_score')

    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                           'jpeg', 'webp', 'gif']),
                    MaxValueValidator(limit_value=1024 * 1024 * 50)])

    def __init__(self, user, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(user=user)


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'platform', 'image', 'user_score',
                  'metacritic_score', 'developer', 'genres', 'release_date',
                  'completion_date', 'hours_spent',  'user_review')


class AddWishlistGameForm(forms.ModelForm):
    class Meta:
        model = WishListGame
        fields = ('name', 'platform', 'image', 'priority', "currency", "cost",
                  "store")

    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                           'jpeg', 'webp', 'gif']),
                    MaxValueValidator(limit_value=1024 * 1024 * 50)])

    def __init__(self, user, *args, **kwargs):
        super(AddWishlistGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(
            user=user)


class EditWishListGameForm(forms.ModelForm):
    class Meta:
        model = WishListGame
        fields = ('name', 'platform', 'image', 'store', 'priority',
                  'developer', 'genres', 'release_date', 'currency', 'cost')
