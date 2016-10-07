from django import forms
from .models import ModelFormModel
class ModelFormForm(forms.ModelForm):
    class Meta:
        model = ModelFormModel
        fields = ["name", "bio"]
