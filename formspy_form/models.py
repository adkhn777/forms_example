from django.db import models

class FormspyFormModel(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=200)
    # str and unicode both are same but unicode prefer str returns bytes unicode returns char
    # def __str__(self):
    #     return 'This is %s' % self.name
    def __unicode__(self):
        return 'This is %s' % self.name
