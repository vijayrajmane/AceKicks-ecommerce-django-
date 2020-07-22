from django.shortcuts import render, redirect
from .models import productReview
from orders.models import product
# Create your views here.

def review(request, productID):
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('review')
        item  =  product.objects.get(id = productID)
        review = productReview(user=request.user, item=item, rating=rating, comment=comment)
        review.save()
        return redirect('/detail/'+ str(productID))