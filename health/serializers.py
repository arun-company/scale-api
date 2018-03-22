from rest_framework import serializers as s
from rest_auth.serializers import UserDetailsSerializer

from health import models as m
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserProfileSerializer(s.ModelSerializer):
    class Meta:
        model = m.UserProfile
        fields = ('account','birthday', 'nickname', 'gender', 'height', 'image', 'state')

class ProfileSerializer(s.ModelSerializer):
    class Meta:
        model = m.UserProfile
        fields = ('account','birthday', 'nickname', 'gender', 'height', 'image', 'state')


class AuthUserSerilaizer(s.ModelSerializer):
#   account = serializers.SlugRelatedField(source = 'health.user_profile')
#   account = serializers.CharField(source='health.user_profile')
  class Meta:
    model = User
    fields = ('email', 'password' )
    write_only_fields = ('password',)


class UserSerializer(UserDetailsSerializer):
    # profileS = ProfileSerializer()
  
    class Meta(UserDetailsSerializer.Meta):
        fields = '__all__'
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        m.UserProfile.objects.create(user=user, **profile_data)
        return user
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.save()

        return instance




class CreateUserSerializer(s.ModelSerializer):
    password = s.CharField(write_only=True)
    email =  s.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])
    
    def validate_password(self, value):
        """
        Check that the blog post is about Django.
        """
        if len(value) < 6:
            raise s.ValidationError("Password Length must me greater or equal 6 chars.")
        return value

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
        return user

class UpdateUserSerial(s.ModelSerializer):
    email =  s.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])
    
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email')

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