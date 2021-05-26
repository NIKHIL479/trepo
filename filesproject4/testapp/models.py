from django.db import models


# Create your models here.
class Student(models.Model):
    image=models.ImageField(upload_to='media/')
    video=models.FileField(upload_to='media/')
  
