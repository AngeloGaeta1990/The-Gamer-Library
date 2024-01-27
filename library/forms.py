from django import forms
from .models import Platform, Game


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image')


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
        fields = EditPlatformForm.Meta.fields + ('subscription_fee', 'plan')


class EditMobilePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = Platform
        fields = EditPlatformForm.Meta.fields + ('brand', 'operative_systems')


class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'platform')

    def __init__(self, user, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)
        # Filter platforms based on the current user
        self.fields['platform'].queryset = Platform.objects.filter(user=user)
