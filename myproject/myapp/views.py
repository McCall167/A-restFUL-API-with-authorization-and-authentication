from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]