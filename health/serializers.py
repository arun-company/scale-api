from rest_framework import serializers as s
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.models import TokenModel
from health import models as m
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class ProfileSerializer(s.ModelSerializer):
    class Meta:
        model = m.UserProfile
        fields = ('account','birthday', 'nickname', 'gender', 'height', 'image', 'state')


class AuthUserSerilaizer(s.ModelSerializer):
  class Meta:
    model = User
    fields = ('email', 'password' )
    write_only_fields = ('password',)

class FamilyProfileSerializer(s.ModelSerializer):
    member_name = s.SerializerMethodField('get_memeber_name')
    class Meta:
        model = m.Profile
        fields = ('profile_id','member_name','secret',)
    def get_memeber_name(self, obj):
        return obj.nickname

class AccountSerializer(s.ModelSerializer):
    class Meta:
        model = m.Account
        fields = ('acc_id','app','carrier', 'username', 'email', 'mobile', 'name')

class WeightSerializer(s.ModelSerializer):
    BMI = s.FloatField(required=True)
    BFR = s.FloatField(required=True)
    BWR = s.FloatField(required=True)
    MMR = s.FloatField(required=True)
    BD = s.FloatField(required=True)
    measured = s.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = m.Weight
        fields = ('weight','BMI','BFR', 'BWR', 'MMR', 'BD', 'measured')

class UserProfileSerializer(s.ModelSerializer):
    profileS = ProfileSerializer()
    class Meta:
        model = User
        fields = ('profileS','email','username')
    
class UserS(s.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')

class UPS(s.ModelSerializer):
    user = UserS(required=True)
    birthday = s.DateTimeField(format='%Y-%m-%d')
    # birthday = s.DateTimeField(format="yyyy-mm-dd", input_formats=None)  
    class Meta:
        model = m.UserProfile
        fields = ('account_id','user', 'birthday', 'gender', 'height','state')

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
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.save()

        return instance


class TokenSerializer(s.ModelSerializer):
    """
    Serializer for Token model.
    """
    token = s.SerializerMethodField('get_token_name')

    class Meta:
        model = TokenModel
        fields = ('token',)
    def get_token_name(self, obj):
        return obj.key

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
        try:
            username = validated_data['username']
        except KeyError:
            username = validated_data['email']
        user = User(
            email=validated_data['email'],
            username=username
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
            user_id=validated_data['user_id'],
        )
        profile.save()
        return profile