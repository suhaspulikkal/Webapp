from django.db import models


class Emails(models.Model):
    email= models.EmailField()
    name= models.CharField(max_length=200)
    subject= models.CharField(max_length=200)
    message= models.TextField()
