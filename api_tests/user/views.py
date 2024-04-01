from django.shortcuts import render
from .serializers import UserDataSerializer, UserDataUsernameSerializer
from rest_framework import viewsets
from .models import Userdata, UserDataUsername
# Create your views here.

class UserDataView(viewsets.ModelViewSet):
    queryset = Userdata.objects.all()
    serializer_class = UserDataSerializer
    
class UserDataUsernameView(viewsets.ModelViewSet):
    queryset = UserDataUsername.objects.all()
    serializer_class = UserDataUsernameSerializer