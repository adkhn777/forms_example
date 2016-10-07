from django.shortcuts import render, HttpResponse
from .forms import ModelFormForm

def index(request):
    form = ModelFormForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('Successfull Submit')
    return render(request, 'model_form/form.html', {
        'form': form
    })
