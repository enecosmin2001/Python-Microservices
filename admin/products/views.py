from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer

from .models import Product, User

import random

class ProductViewSet(viewsets.ViewSet):


    def list(self, request): # GET /api/products 
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


    def create(self, request): # POST /api/products 
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrive(self, request, pk=None): # GET /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def update(self, request, pk=None): # PUT /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None): # DELETE /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):


    def get(self, _): # GET /api/users 
        users = User.objects.all()

        if len(users) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)

        user = random.choice(users)
        return Response({
            'id': user.id
        })