from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Userdata, UserDataUsername
from rest_framework import serializers

class UserDataUsernameSerializer(ModelSerializer):
    class Meta:
        model = UserDataUsername
        fields = "__all__"

class UserDataSerializer(ModelSerializer):
    username = serializers.StringRelatedField()

    class Meta:
        model = Userdata
        fields = ('id', 'first_name', 'last_name', 'username')
