from django.db import models
from django.utils import timezone


#class Post(models.Model):
#    author = models.ForeignKey('auth.User')
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(
#            default=timezone.now)

#    def __str__(self):
#        return self.title


class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    link_title = models.CharField(max_length=200, default="Source Code")
    link = models.CharField(max_length=200, default="default")
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title


class About(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default="default")
    text = models.TextField()
    email = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200, default="default")
    github = models.CharField(max_length=200, default="default")

    def __str__(self):
        return self.title


class FrontPage(models.Model):
    title = models.CharField(max_length=200, default="default")

    def __str__(self):
        return self.title
