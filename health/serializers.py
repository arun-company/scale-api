from rest_framework import serializers
from health.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'account','birthday', 'nickname', 'gender', 'height', 'image', 'state')

# class UserSerializer(serializers.ModelSerializer):
#     city = serializers.CharField(source='myuser.city')
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'city')