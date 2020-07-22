from django.db import models
from django.contrib.auth.models import User
from orders.models import product
# Create your models here.

class productReview(models.Model):
    user = models.ForeignKey(User,related_name='reviews', on_delete=models.CASCADE, null=True,blank=True)
    item = models.ForeignKey(product, on_delete = models.CASCADE, null=True,blank=True) 
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()