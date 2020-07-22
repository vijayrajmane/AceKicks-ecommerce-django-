from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from orders.models import category,brand,size,gender,product,orderMaster,orderDetail,orderStatus,cartItem
from orders.serializers import UserSerializer, ProductSerializer, GenderSerializer,BrandSerializer,CategorySerializer,SizeSerializer
from review.models import productReview
from review.serializer import ReviewSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse
from rest_framework import generics

@api_view(['GET','POST'])
def UserList(request, format=None):
    if request.method == 'GET':
        try:
            item = User.objects.all()
            
        except product.DoesNotExist:
            raise Response(status = 404)
    
        serializer = UserSerializer(item, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def UserDetail(request,pk, format=None):
     if request.method == 'GET':
        try:
            item = User.objects.filter(pk=pk)   
        except product.DoesNotExist:
            raise Response(status = 404)
    
        serializer = UserSerializer(item, many=True)
        return Response(serializer.data)


class ListView(generics.ListCreateAPIView):
    queryset = productReview.objects.all()
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET','POST'])
@csrf_exempt
def ItemReview(request,ID, format=None):

    if request.method == 'GET':
        try:
            item = product.objects.get(id=ID)
            review= productReview.objects.filter(item = item)
        except product.DoesNotExist:
            raise Response(status = 404)
    
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.save(user = request.user)
            return Response({'success': True}, status=201)
        return Response(serializer.errors, status=400)

