from django.db import models

# Create your models here.


class signup_details(models.Model):
    email=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    desination=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
  
