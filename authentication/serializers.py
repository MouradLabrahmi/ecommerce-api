from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=40,allow_blank=True)
    email=serializers.EmailField(max_length=40,allow_blank=False)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)
    gender = serializers.IntegerField(allow_null=True)


    class Meta:
        model=User
        fields=['id','username', 'email', 'phone_number','password','gender']

    def validate(self,attrs):
        if User.objects.filter(username=attrs.get('username')).exists():

            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        if User.objects.filter(email=attrs.get('email')).exists():

            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        if User.objects.filter(phone_number=attrs.get('phone_number')).exists():
            
            raise ValidationError(detail="User with phone number exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)


    def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']