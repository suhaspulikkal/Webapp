
from django.db import models

# Create your models here.
class Certificates(models.Model):
    date = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='images')
    company = models.CharField(max_length=200)
    show = models.BooleanField(default=False)