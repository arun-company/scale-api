from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from health import models as m
from django.views.decorators.csrf import csrf_exempt
from health import serializers as s
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import status
import json
import re

class UserViewList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = m.User.objects.all().order_by('created')
    serializer_class = s.UserSerializer

class UserList(APIView):

    def get(self, request):
        # user = request.user
        users = User.objects.all()
        serializer = s.UserSerializer(users, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

class UserInfo(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, account_id):
        # return Response({'account_id': account_id})
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        # self.check_object_permissions(request, zone)
        serializer = s.UPS(profile)
        return Response(serializer.data)
    def put(self, request, account_id, format=None):
        data = request.data
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        print (profile)
        if (profile):
            user_id = profile.user_id
            username = data['username']
            m.User.objects.filter(id=user_id).update(username=username)
            serializer = s.UPS(profile)
            return Response(serializer.data)

        serializer = s.UPS(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, account_id):
        user = get_object_or_404(User, id=pk)
        data = request.data
        serializer = s.CreateUserSerializer(user,data=data)
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({
                "messesge": "Update Fail!"
            }, 400)
    def delete(self, request, account_id):
        # user = get_object_or_404(User, id=pk)
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        if profile.delete():
            return Response({
                "result": True
            }, 200)
        return Response({
            "result": False
        }, 400)

class UserRegister(APIView):
    def get(self, request):
        users = User.objects.all()
        # self.check_object_permissions(request, zone)
        serializer = s.AuthUserSerilaizer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        if (request.META.get('HTTP_REQUESTOR_ID') == "23810e1b-21c4-46fd-9e8e-e22156dbeb39"):
            data = request.data
            print(data)
            serialized = s.CreateUserSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
                new_user = dict(serialized.data)
                user_id = new_user.get('id')
                print(user_id)
                if user_id:
                    profile = m.UserProfile(
                        birthday="2010-10-10 01:01",
                        user_id=user_id
                    )
                    profile.save()
                    return Response({
                                "account_id": profile.account_id
                            }, status=200)
                else :
                    u = User.objects.get(id = user_id)
                    u.delete()
                    return Response(serialized._errors, status=400)    
            else: 
                return Response(serialized._errors, status=400)
        else:
            return Response({
                "Result": "Not Allow!"
            }, 500)

class UserSignin(APIView):
    def post(self, request):
        
        serializer = s.TokenSerializer(request.data)
        serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()



class ExistingMember(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, pk):
        data = request.data
        member = get_object_or_404(m.Account, email=data['email'])
        if member:
            return Response({
                "status" : "Success!",
                "message": data['email'] + " is an existing member."
            })
        else:
            return Response({
                "status" : "Success!",
                "message": data['email'] + " is an existing member."
            })
        return Response(request.data)
        user = get_object_or_404(User, id=pk)
        # self.check_object_permissions(request, zone)
        serializer = s.UserSerializer(user)
        return Response(serializer.data)


class MigrateOldAccount(APIView):
    def post(self, request, account_id):
        # return Response(request.data)
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        data = request.data
        # return Response(data)
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        if EMAIL_REGEX.match(data['email']):
            oldUser = m.Account.objects.filter(email=data['email'], password=data['password'])
            if (oldUser):
                serializer = s.AccountSerializer(oldUser, many=True)
                # TODO: weights at weights table and replace the account with the current user. Delete the account from the Chinese account table.
                return Response({
                    "accountConfirmed": True,
                    "accountType": 1
                })
        else:
            oldUser = m.Family.objects.filter(email=data['email'])
            if (oldUser):
                family_no = oldUser[0].family_no
                # print(family_no)
                allProfile = m.Profile.objects.filter(family_no=family_no)
                serializer = s.FamilyProfileSerializer(allProfile, many=True)
                #2. Health Plus DB : return the list of members that belong to this account, return True for accountConfirmed, return 2 for accountType.
                return Response({
                    "accountConfirmed": True,
                    "accountType": 2,
                    "familyMembers": serializer.data
                })
        # print(oldUser)
        if (oldUser):
            return Response({
                "message": "Migrate Successfully!"
            })
        return Response({
            "message": "User infomation provide is incorrect!"
        }, 404)


class MigrateOldFamilyMember(APIView):
    def post(self, request, account_id):
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        data = request.data
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        if EMAIL_REGEX.match(data['family_email']):
            oldUser = m.Account.objects.filter(email=data['family_email'], password=data['family_password'])
            if (oldUser):
                serializer = s.AccountSerializer(oldUser, many=True)
                # TODO: weights at weights table and replace the account with the current user. Delete the account from the Chinese account table.
                return Response({
                    "accountConfirmed": True,
                    "accountType": 1
                })
        else:
            oldUser = m.Family.objects.filter(email=data['family_email'], password=data['family_password'])
            if (oldUser):
                family_no = oldUser[0].family_no
                # print(family_no)
                allProfile = m.Profile.objects.filter(family_no=family_no, nickname= data['member_name'])
                for pro in allProfile:
                    m.Weight.objects.filter(account_id=pro.profile_id).update(account_id=profile.account_id, legacy=0)
                    pro.delete()
                #2. Health Plus DB : return the list of members that belong to this account, return True for accountConfirmed, return 2 for accountType.
                return Response({
                    "familyMemberConfirmed": True,
                })
        return Response(request.data)
        # self.check_object_permissions(request, zone)
        serializer = s.UserSerializer(user)
        return Response(serializer.data)

