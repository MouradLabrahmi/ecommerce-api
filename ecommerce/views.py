from django.shortcuts import render,get_object_or_404
from .models import Category, Product, Cart, CartItem
from rest_framework.views import APIView
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404





User = get_user_model()

class CategoryView(generics.GenericAPIView):
    serializer_class=serializers.CategorySerializer

    @swagger_auto_schema(operation_summary="Get all Caterogies (without authentication)")
    def get(self,request):
        categories=Category.objects.all()

        serializer=self.serializer_class(instance=categories,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)


class DetailCategory(generics.GenericAPIView):
    serializer_class=serializers.CategorySerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary="View the detail of a category by its ID (without authentication)")
    def get(self, request,pk):


        category = self.get_object(pk)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ProductView(APIView):
    serializer_class=serializers.ProductSerializer

    @swagger_auto_schema(operation_summary="Get all Products (without authentication)")
    def get(self,request):
        products=Product.objects.all()
        serializer=self.serializer_class(instance=products,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)


class DetailProduct(generics.GenericAPIView):
    serializer_class=serializers.ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary="View the detail of a product by its ID (without authentication)")
    def get(self, request,pk):


        product = self.get_object(pk)
        serializer = serializers.CategorySerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FilterProductsByCategory(generics.GenericAPIView):
    serializer_class=serializers.ProductSerializer
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary="Filter products by category (without authentication)")
    def get(self,request,categ_id):

        category=self.get_object(categ_id)
        
        products=Product.objects.all().filter(category=category)

        serializer=self.serializer_class(instance=products,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

class AddCartView(generics.GenericAPIView):
    serializer_class=serializers.CartItemSerializer
    permission_classes=[IsAuthenticated]

        
    @swagger_auto_schema(operation_summary="Add product to cart (with authentication)")
    def post(self,request, *args, **kwargs):
        
        user = request.user
        cart = get_object_or_404(Cart, user=user.id)
        product = get_object_or_404(Product, pk=request.data["product"])
        quantity = int(request.data["quantity"])
        
        if quantity > product.quantity:
            raise NotAcceptable("You order quantity more than the seller have")
        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        cart_item.save()
        serializer = serializers.CartItemSerializer(cart_item)
        total = float(product.price) * float(quantity)
        cart.total = total
        cart.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartDeleteItem(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(operation_summary="Delete an Item from cart by its ID (with authentication)")
    def delete(self, request,cartitem_id):
        
        cartitem =get_object_or_404(CartItem,id=cartitem_id)

        cartitem.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
