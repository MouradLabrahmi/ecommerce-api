from rest_framework import serializers
from .models import Category, Product, Cart,CartItem
from django.contrib.auth.models import User




class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required = True, allow_blank=True, max_length=250)
    class Meta:
        model = Category 
        fields = ['id','name']
        




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','category']
            
        


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'products',
        )

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "quantity"]