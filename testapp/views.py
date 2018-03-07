from django.shortcuts import render
from django.contrib.auth.models import User
from testapp.models import Amenity
from rest_framework import viewsets
from testapp.serializers import UserSerializer, AmenitySerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all().order_by('eng_name')
    serializer_class = AmenitySerializer

