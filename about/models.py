from django.db import models

# Create your models here.
class About(models.Model):

    bio  = models.CharField(max_length=200)

    name  = models.CharField(max_length=200)

    para1  = models.TextField()

    para2  = models.TextField()

    date = models.CharField(max_length=200)

    number = models.CharField(max_length=200)

    nationality  = models.CharField(max_length=200)

    religion  = models.CharField(max_length=200)

    status  = models.CharField(max_length=200)

    skills  = models.CharField(max_length=200)

    skill1  = models.CharField(max_length=200)

    skill1per = models.CharField(max_length=200)

    skill2 = models.CharField(max_length=200)

    skill2per  = models.CharField(max_length=200)

    skill3 = models.CharField(max_length=200)

    skill3per = models.CharField(max_length=200)

    skill4  = models.CharField(max_length=200)

    skill4per  = models.CharField(max_length=200)

    whychooseme_title1  = models.CharField(max_length=200)

    whychooseme_title2 = models.CharField(max_length=200)

    whychooseme_title3  = models.CharField(max_length=200)

    whychooseme_title1_desc  = models.CharField(max_length=200)

    whychooseme_title2_desc  = models.CharField(max_length=200)

    whychooseme_title3_desc = models.CharField(max_length=200)

    img = models.ImageField(upload_to='images')

    show = models.BooleanField(default=False)

    def __str__(self):

        return  self.name