from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    Name=models.CharField(max_length=30)