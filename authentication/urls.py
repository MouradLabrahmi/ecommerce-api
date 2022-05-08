from django.urls import path
from . import views
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
app_name = "authentication"

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('signup/',views.UserSerializer.as_view(),name='sign_up')
]