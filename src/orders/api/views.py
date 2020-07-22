from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt,  csrf_protect

from orders.models import category, brand, size, gender, product, orderMaster, orderDetail, orderStatus, cartItem
from review.models import productReview
from orders.serializers import UserSerializer, ProductSerializer, GenderSerializer, BrandSerializer, CategorySerializer, SizeSerializer, OrderSerializer, OrderDetailSerializer, CartItemSerializer, StatusSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse


@api_view(['GET'])
def Product_Detail(request, productID, format=None):

    if request.method == 'GET':
        try:
            item = product.objects.filter(id=productID)
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = ProductSerializer(item, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def filterProduct(request, format=None):

    if request.method == 'GET':
        try:
            items = gender.objects.all()
            Brand = brand.objects.all()
            Category = category.objects.all()
        except product.DoesNotExist:
            raise Response(status=404)
        data = {}
        serializer = GenderSerializer(items, many=True)
        data['gender'] = serializer.data
        serializer = BrandSerializer(Brand, many=True)
        data['brand'] = serializer.data
        serializer = CategorySerializer(Category, many=True)
        data['category'] = serializer.data

        return Response(data)


@api_view(['GET'])
def genderShoe(request, genID, format=None):

    if request.method == 'GET':
        try:
            items = product.objects.filter(gender=genID)
        except product.DoesNotExist:
            raise Response(status=404)

        serializer = ProductSerializer(
            items, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def brandShoe(request, brandID, format=None):

    if request.method == 'GET':
        try:
            items = product.objects.filter(brand=brandID)
        except product.DoesNotExist:
            raise Response(status=404)

        serializer = ProductSerializer(items, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def categoryShoe(request, catID, format=None):

    if request.method == 'GET':
        try:
            items = product.objects.filter(category=catID)
        except product.DoesNotExist:
            raise Response(status=404)

        serializer = ProductSerializer(items, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def detailPage(request, productID, format=None):

    if request.method == 'GET':
        try:
            items = product.objects.filter(id=productID)
            Size = size.objects.all()
        except product.DoesNotExist:
            raise Response(status=404)
        data = {}
        serializer = ProductSerializer(items, many=True)
        data['product'] = serializer.data
        serializer = SizeSerializer(Size, many=True)
        data['size'] = serializer.data
        data['success'] = True
        return Response(data)


@api_view(['GET'])
def myOrder(request):

    if request.method == 'GET':
        try:
            order = orderMaster.objects.filter(user=request.user)
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def myOrderDetail(request, orderID):

    if request.method == 'GET':
        try:
            order = orderMaster.objects.get(id=orderID)
            productDetail = orderDetail.objects.filter(order=order)
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = OrderDetailSerializer(productDetail, many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def ConfirmOrder(request, format=None):

    if request.method == 'GET':

        try:
            order = orderMaster.objects.all()

        except product.DoesNotExist:
            raise Response(status=404)


        serializer = OrderSerializer(order, many = True)

        return Response(serializer.data)


    if request.method == 'POST':

        try:
            cart = cartItem.objects.filter(user=request.user)

        except product.DoesNotExist:
            raise Response(status=404)


        serializer = OrderSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            data = {}
            master = serializer.save(user=request.user)
            data['success']=True
            data['masterID'] = master.id
            return Response(data)
        return Response(     status = 400)



@api_view(['POST'])
def ConfirmOrderDetail(request, format=None):

    if request.method == 'POST':
        print(request.data)
        try:
            cart = cartItem.objects.filter(user=request.user)

        except product.DoesNotExist:
            raise Response(status=404)

        for x in cart:
            serializer = OrderDetailSerializer(data=request.data)
        
            if serializer.is_valid():
                data = {}
                detail = serializer.save(product = x.item, price = x.item.price, Shoesize = x.Shoesize)
                data['success'] = True
                

        cart.delete()       
        return Response(data)
        


@api_view(['GET', 'POST'])
def cart(request, format=None):
    if request.method == 'GET':
        try:
            cart = cartItem.objects.filter(user=request.user)
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = CartItemSerializer(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print('*******************')
        print(request.data)
        serializer = CartItemSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            cart = serializer.save(user=request.user)
            data['success'] = True
            data['data'] = serializer.data
            return Response(data, status=201)
        return Response(serializer.error, status=400)


@api_view(['GET', 'DELETE'])
def cartDetail(request, rowID):

    try:
        cart = cartItem.objects.get(id=rowID)
        print(cart)
    except product.DoesNotExist:
        raise Response(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        print(request.data)
        print(rowID)
        print(cart)
        cart.delete()
        data = {}
        data['success'] = True
        return Response(data)

@api_view(['GET'])
def OrderList(request):

    if request.method == 'GET':
        try:
            order = orderMaster.objects.all()
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def StatusList(request):

    if request.method == 'GET':
        try:
            x = orderStatus.objects.all()
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = StatusSerializer(x, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def StatusDetail(request, pk):

    if request.method == 'GET':
        try:
            x = orderStatus.objects.filter(pk = pk)
        except product.DoesNotExist:
            raise Response(status=404)
        serializer = StatusSerializer(x, many=True)
        return Response(serializer.data)

@api_view(['PATCH'])
def ChangeStatus(request,orderID, format=None):

    if request.method == 'PATCH':

        try:
            master = orderMaster.objects.get(id = orderID)
        except product.DoesNotExist:
            raise Response(status=404)
        print(master)
        print(request.data)
        # master.status = x
        # master.save()
        # return JsonResponse(
        #     {
        #         'success':True
        #     }
        # )
        serializer = OrderSerializer(master, data=request.data, partial=True)
        
        if serializer.is_valid():
            
            data = {}
            #print(serializer.status )
            b = serializer.save()
           # b = serializer.update(master, request.data)
            
            print(b)
            data['success']=True
            #data['data'] = b
            return Response(data)
        return Response ( status=400)


