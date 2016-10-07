from django.db import models

class ModelFormModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
