from django.db import models

# Create your models here.
from django.db import models


class Works(models.Model):
    title = models.CharField(max_length=100, blank=False)
    startDate = models.DateField(blank=False)
    pin=models.BooleanField(blank=True,default=False)
    endDate = models.DateField(blank=True)
    isOngoing = models.BooleanField(blank=True, default=True)
    desc = models.TextField(blank=False)
    images = models.TextField(blank=False)
    tools = models.TextField(blank=False)
    language = models.TextField(blank=False)
    keyPoints = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True)
    github = models.URLField(blank=True)
    download = models.URLField(blank=True)


class Social(models.Model):
    site = models.CharField(max_length=50, blank=False)
    icon = models.CharField(max_length=50, blank=False)
    link = models.URLField(blank=False)


class MyInfo(models.Model):
    image=models.TextField()
    tag=models.CharField(max_length=100)
    intro=models.TextField()
    about = models.TextField()
    email = models.CharField(max_length=70, blank=True)
    phone = models.CharField(max_length=20, blank=True)

class Skills(models.Model):
    skillName=models.CharField(max_length=30)
    percentage=models.IntegerField()
