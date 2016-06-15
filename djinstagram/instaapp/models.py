from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    owner = models.ForeignKey(User, null=True)
    caption = models.TextField(max_length=255)
    path = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.path

class Like(models.Model):
    owner = models.ForeignKey(User, null=True)
    photo = models.ForeignKey(Photo, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo

class Tag(models.Model):
    name = models.TextField(max_length=255)
    photo = models.ManyToManyField(Photo)

    def __str__(self):
        return self.name
