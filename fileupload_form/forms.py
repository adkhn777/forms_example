from django import forms
from .models import FileUploadFormModel
class FileUploadFormForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()

class FileUploadFormModelForm(forms.ModelForm):
    class Meta:
        model = FileUploadFormModel
        fields = ['name', 'file']
