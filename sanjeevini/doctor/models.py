from django.db import models

# Create your models here.

class doctor_register(models.Model):
    Name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    number=models.BigIntegerField()
    address=models.CharField(max_length=200)
    #image=models.ImageField(upload_to='pics')
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    idc=models.BooleanField(default=False)