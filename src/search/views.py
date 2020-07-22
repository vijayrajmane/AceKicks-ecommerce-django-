from django.shortcuts import render, redirect

from orders.models import product, cartItem
# Create your views here.

def search_view(request):
    query = request.GET.get('q', None)
    itemCount =  cartItem.objects.filter( user = request.user).count()
    if query is not None:
        productList = product.objects.search(query = query)
        context = {
            'productList': productList,
            'query': query,
            'count': itemCount,
        }
        return render(request, 'search/view.html', context)
    else:
        return redirect('/')