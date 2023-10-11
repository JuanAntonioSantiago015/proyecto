# URL
# from django.shortcuts import render
from django.shortcuts import get_object_or_404

# API
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status

# SERIALIZER
from .serializers import UserSerializer

# MODELOS
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
