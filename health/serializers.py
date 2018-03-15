from rest_framework import serializers
from health.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'account', 'username', 'email', 'nickname', 'gender', 'height', 'image', 'state')