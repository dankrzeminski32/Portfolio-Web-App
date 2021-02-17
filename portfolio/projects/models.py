from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    link = models.CharField(max_length=140, default = 'DEFAULT VALUE')
    image = models.FilePathField(path="/img")
