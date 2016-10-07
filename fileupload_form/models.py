from django.db import models

class FileUploadFormModel(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField()
