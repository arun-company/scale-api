from rest_framework import serializers as s
from rest_auth.serializers import UserDetailsSerializer

from health import models as m
from django.contrib.auth.models import User

class UserProfileSerializer(s.ModelSerializer):
    class Meta:
        model = m.UserProfile
        fields = ('id', 'account','birthday', 'nickname', 'gender', 'height', 'image', 'state')


class AuthUserSerilaizer(s.ModelSerializer):
#   account = serializers.SlugRelatedField(source = 'health.user_profile')
#   account = serializers.CharField(source='health.user_profile')
  class Meta:
    model = User
    fields = ('email', 'password' )
    write_only_fields = ('password',)


class UserSerializer(UserDetailsSerializer):

    account = s.CharField(source="userprofile.account")
    nickname = s.CharField(source="userprofile.nickname")
    image = s.CharField(source="userprofile.image")
    state = s.IntegerField(source="userprofile.state")
    gender = s.IntegerField(source="userprofile.gender")
    birthday = s.DateTimeField(source="userprofile.birthday")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('account','nickname','gender','image','state','birthday',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        account = profile_data.get('account')
        nickname = profile_data.get('nickname')
        image = profile_data.get('image')
        state = profile_data.get('state')
        birthday = profile_data.get('birthday')
        gender = profile_data.get('gender')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.UserProfile
        if profile_data:
            profile.account = account
            profile.nickname = nickname
            profile.state = state
            profile.image = image
            profile.gender = gender
            profile.birthday = birthday
            profile.save()
        return instance



class CreateUserSerializer(s.ModelSerializer):
    password = s.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user;

class CreateProfileSerialzer(s.ModelSerializer):
    class Meta: 
        model = m.UserProfile
        fields = ('id', 'account','birthday', 'nickname', 'gender', 'height', 'image', 'state', 'user_id')
    def create(self, validated_data):
        profile = m.UserProfile(
            account=validated_data['account'],
            birthday=validated_data['birthday'],
            nickname=validated_data['account'],
            user_id=validated_data['user_id'],
        )
        profile.save()
        return profile

# class UserSerializer(serializers.ModelSerializer):
#     city = serializers.CharField(source='myuser.city')
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'city')