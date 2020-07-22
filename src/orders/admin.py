from django.contrib import admin
from .models import category,brand,size,gender,product,orderMaster,orderDetail,orderStatus,cartItem
# Register your models here.
admin.site.register(category)
admin.site.register(brand)
admin.site.register(size)
admin.site.register(gender)
admin.site.register(orderStatus)
admin.site.register(product)
admin.site.register(orderMaster)
admin.site.register(orderDetail)
admin.site.register(cartItem)