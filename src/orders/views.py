from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt

from .models import category,brand,size,gender,product,orderMaster,orderDetail,orderStatus,cartItem
from review.models import productReview
from .serializers import UserSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer

def index(request):
    cat = category.objects.all()
    shoeBrand = brand.objects.all()
    gen = gender.objects.all()
    if request.user.is_authenticated:
        itemCount =  cartItem.objects.filter( user = request.user).count()
        context2 = {
                'cat': cat,
                'shoeBrand':shoeBrand,
                'gen':gen,
                'count': itemCount,
            }
        return render(request, 'orders/index.html',context2)
    context = {
        'cat': cat,
        'shoeBrand':shoeBrand,
        'gen':gen,
    }
    return render(request, 'orders/index.html',context)

@csrf_exempt
def login_view(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request,user)
        return JsonResponse({
                'success': True
            })
    else:
        return JsonResponse({
            'success': False
        })


@api_view(['POST'])
def userRegister(request):
    print(request.data)
    if request.method == 'POST':
        serializer  = UserSerializer(data = request.data )
        data = {}
        if serializer.is_valid():
            account =  serializer.save()
            data['response'] = 'success'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


def logout_view(request):
    logout(request)
    return redirect('/')

def genderShoe(request, genID, format=None):
    if request.user.is_authenticated:
        itemCount =  cartItem.objects.filter( user = request.user).count()
        context2 = {
                'count':itemCount,
            }
        return render(request, "orders/productList.html", context2)
    return render(request, 'orders/productList.html')


def brandShoe(request, brandID, format=None):
    if request.user.is_authenticated:
        itemCount =  cartItem.objects.filter( user = request.user).count()
        context2 = {
                'count':itemCount,
            }
        return render(request, "orders/productList.html", context2)
    return render(request, 'orders/productList.html')


def categoryShoe(request, catID, format=None):
    if request.user.is_authenticated:
        itemCount =  cartItem.objects.filter( user = request.user).count()
        context2 = {
                'count':itemCount,
            }
        return render(request, "orders/productList.html", context2)
    return render(request, 'orders/productList.html')

def detailPage(request, productID,format=None):
    if request.user.is_authenticated:
        itemCount =  cartItem.objects.filter( user = request.user).count()
        context2 = {
                'count':itemCount,
            }
        return render(request, "orders/detail.html", context2)
    return render(request, 'orders/detail.html')


def cartPage(request, format=None):
    
    return render(request, 'orders/cart.html')


def checkoutPage(request, format=None):

    return render(request, 'orders/checkout.html' )


def myOrders(request):
    itemCount =  cartItem.objects.filter( user = request.user).count()
    context = {
        'count':itemCount,
    }
    return render(request, 'orders/myorders.html', context)


def manageOrder(request):

    return render(request, 'orders/manageOrder.html')

