from django import forms

class FormsetFormForm(forms.Form):
    name = forms.CharField(max_length=20)
    bio = forms.Textarea(max_length=200)

class FormssetFormFormTwo

FormsetFormFormSet = forms.formset_factory(FormsetFormForm)