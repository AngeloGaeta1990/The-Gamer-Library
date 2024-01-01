from .models import Platform
from .models import Game
from django import forms


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name','category')



class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name','platform')