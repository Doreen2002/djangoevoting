from django.db import models

# Create your models here.
class Rcandidates(models.Model):
    organ = models.TextField()
    position = models.TextField()
    intake = models.TextField()
    course = models.TextField()
    studentno = models.IntegerField()
class Rvoters(models.Model):
    username = models.TextField()
    password = models.CharField(max_length=10)
    confirmpassword = models.CharField(max_length=10)