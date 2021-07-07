from django.db import models
from django.db.models import fields

# Create your models here.
class Product(models.Model):
    product_name = fields.CharField(max_length=50)
    list_price = fields.FloatField()
    description = fields.TextField(max_length=300)
    photo = models.ImageField(upload_to='products')