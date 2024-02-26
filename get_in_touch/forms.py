from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form for CollaborateRequest model.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
