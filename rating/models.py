from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()


class technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()


class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='projects/')
    description = models.CharField(max_length=255)
    live_link = models.CharField(max_length=255)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall = models.IntegerField(blank=True,default=0)
    categories = models.ManyToManyField(categories)
    technologies = models.ManyToManyField(technologies)
    posted  = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title