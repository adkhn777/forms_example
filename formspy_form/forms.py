from django import forms

class FormspyFormForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}), required=False)
    bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Bio'}), required=False)
