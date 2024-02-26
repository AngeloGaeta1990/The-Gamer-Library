from django.core.validators import FileExtensionValidator
from django import forms
from .models import Platform, Game, WishListGame


class AddPlatformForm(forms.ModelForm):
    """
    Form for adding a new platform.
    """
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image')

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])]
    )


class EditPlatformForm(forms.ModelForm):
    """
    Form for editing a platform.
    """
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image', 'background_color',
                  'font_color')

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])])


class EditPCPlatformForm(EditPlatformForm):
    """
    Form for editing a PC platform.
    """
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('operative_systems', 'gpu',
                                                 'cpu', 'ram', 'disk_size',
                                                 'disk_type')


class EditConsolePlatformForm(EditPlatformForm):
    """
    Form for editing a console platform.
    """
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('model',)


class EditServicePlatformForm(EditPlatformForm):
    """
    Form for editing a service platform.
    """
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('currency',
                                                 'subscription_fee',
                                                 'plan')


class EditMobilePlatformForm(EditPlatformForm):
    """
    Form for editing a mobile platform.
    """
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('brand', 'operative_systems')


class AddGameForm(forms.ModelForm):
    """
    Form for adding a new game.
    """
    class Meta:
        model = Game
        fields = ('name', 'platform', 'image', 'user_score')

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])])

    def __init__(self, user, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(user=user)


class EditGameForm(forms.ModelForm):
    """
    Form for editing a game.
    """
    class Meta:
        model = Game
        fields = ('name', 'platform', 'image', 'user_score',
                  'metacritic_score', 'developer', 'genres', 'release_date',
                  'completion_date', 'hours_spent',  'user_review')

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])])


class AddWishlistGameForm(forms.ModelForm):
    """
    Form for adding a new game to the wishlist.
    """
    class Meta:
        model = WishListGame
        fields = ('name', 'platform', 'image', 'priority', "currency", "cost",
                  "store")

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])])

    def __init__(self, user, *args, **kwargs):
        super(AddWishlistGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(
            user=user)


class EditWishListGameForm(forms.ModelForm):
    """
    Form for editing a game in the wishlist.
    """
    class Meta:
        model = WishListGame
        fields = ('name', 'platform', 'image', 'store', 'priority',
                  'developer', 'genres', 'link', 'release_date', 'currency',
                  'cost')

    image = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg',
                                                               'jpeg', 'webp',
                                                               'gif'])])
