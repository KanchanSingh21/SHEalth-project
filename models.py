from django.db import models

# Create your models here.
class login_details(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)