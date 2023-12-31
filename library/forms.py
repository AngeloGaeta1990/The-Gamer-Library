from .models import Platform, PCPlatform, ConsolePlatform, ServicePlatform, MobilePlatform, Game

from django import forms


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name','category')

class EditPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name', 'category', 'image', 'box_color', 'font_color')

class EditPCPlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = PCPlatform
        fields = EditPlatformForm.Meta.fields + ('operative_systems', 'gpu', 'cpu', 'ram', 'disk_size', 'disk_type')

class EditConsolePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = ConsolePlatform
        fields = EditPlatformForm.Meta.fields + ('model',)

class EditServicePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = ServicePlatform
        fields = EditPlatformForm.Meta.fields + ('subscription_fee', 'plan')

class EditMobilePlatformForm(EditPlatformForm):
    class Meta(EditPlatformForm.Meta):
        model = MobilePlatform
        fields = EditPlatformForm.Meta.fields + ('brand', 'operative_systems')

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name','platform')