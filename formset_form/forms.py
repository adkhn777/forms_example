from django import forms
from .models import FormsetFormModel
class FormsetFormForm(forms.ModelForm):
    class Meta:
        model = FormsetFormModel
        fields = ['name', 'bio']

FormsetFormFormSet = forms.formset_factory(FormsetFormForm, extra=5)
