from django.db import models

class FormsetFormModel(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
