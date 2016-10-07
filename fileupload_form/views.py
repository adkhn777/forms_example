from django.shortcuts import render, HttpResponse
from .forms import FileUploadFormForm, FileUploadFormModelForm
from .models import FileUploadFormModel
def index(request):
    if request.method == 'POST':
        #
        # This Is The Basic Form Method
        #
        # form = FileUploadFormForm(request.POST, request.FILES)
        form = FileUploadFormModelForm(request.POST, request.FILES)
        if form.is_valid():
            #
            # The Use Of This Function Is Describe Below
            #
            # handle_file_upload(request.FILES['file'])
            form.save()
            return HttpResponse('Successfully Uploaded')
    else:
        form = FileUploadFormModelForm()
    return render(request, 'fileupload_form/form.html', {
        'form': form
    })


#
# This Function Is Used To Upload File In A Specific Location Outside Of Database Models
#
# def handle_file_upload(file):
#     FILE_PATH = 'Example.txt'
#     FILE_MODE = 'wb+'
#     with open(FILE_PATH, FILE_MODE) as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
