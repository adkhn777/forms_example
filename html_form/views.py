from django.shortcuts import render
from .models import HtmlFormModel
def index(request):
    if request.method == 'POST':
        print request.POST['name']
        print request.POST['bio']
        name = request.POST['name']
        bio = request.POST['bio']
        db = HtmlFormModel()
        db.name = name
        db.bio = bio
        db.save()
    return render(request, 'html_form/form.html', {})
