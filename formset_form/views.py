from django.shortcuts import render
from .forms import FormsetFormFormSet
# Create your views here.
def index(request):
    form = FormsetFormFormSet()
    return render(request, 'formset_form/form.html', {
        'form': form
    })
