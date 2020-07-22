from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category (models.Model):
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class brand(models.Model):
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class size(models.Model):
    size =models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return f"{self.size}"

class gender(models.Model):
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return f"{self.gender}"

class orderStatus(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class productQuerySet(models.QuerySet):
    def search(self, query):
        return self.filter(name__iexact = query)

class productManager(models.Manager):
    def get_queryset(self):
        return productQuerySet(self.model, using = self._db )

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    brand = models.ForeignKey(brand , on_delete=models.CASCADE)
    gender = models.ForeignKey(gender, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='image/')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()  

    objects = productManager()
    def __str__(self):
        return f"{self.id} {self.name} {self.category} "

class orderMaster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True )
    status = models.ForeignKey(orderStatus , default=1, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.user} {self.amount} {self.status}  "

class orderDetail(models.Model):
    order = models.ForeignKey(orderMaster, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    Shoesize = models.DecimalField(max_digits=3,decimal_places=1, null=True, blank=True)
    def __str__(self):
        return f"{self.id} {self.order} {self.product} {self.price}  "

class cartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    Shoesize = models.DecimalField(max_digits=3,decimal_places=1, null=True, blank=True)
    def __str__(self):
        return f"{self.id} {self.user} {self.item}  " 
