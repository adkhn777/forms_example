from django.db import models

class HtmlFormModel(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200)
