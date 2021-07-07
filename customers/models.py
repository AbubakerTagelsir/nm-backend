from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='customers')
    