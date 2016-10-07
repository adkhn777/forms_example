from django.shortcuts import render, HttpResponse
from .forms import FormspyFormForm
from .models import FormspyFormModel

def index(request):
    form = FormspyFormForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            bio = form.cleaned_data.get('bio')
            db = FormspyFormModel()
            db.name = name
            db.bio = bio
            db.save()
            return HttpResponse('Successfully Submitted')
    return render(request, 'formspy_form/form.html', {
        'form': form
    })
