from .models import User
from rest_framework import generics,status
from .serializers import UserCreationSerializer, UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class UserSerializer(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="User account creation by signing Up")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    permission_classes=[IsAuthenticated,IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated,IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer