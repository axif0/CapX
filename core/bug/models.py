from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Bug(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    bugTitle = models.TextField(max_length=200)
    slug = models.SlugField(unique=True)
    bugDescription = models.TextField()
    tag = models.CharField(max_length=50)
    subscribers = models.CharField(max_length=200)
    assign_to = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bugTitle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bugTitle