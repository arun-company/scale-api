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

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        # self.check_object_permissions(request, zone)
        serializer = s.UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        user = get_object_or_404(User,id=pk)
        serializer = s.UpdateUserSerial(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
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
    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        if user.delete():
            return Response({
                "messesge": "Delete Successfully!"
            }, 200)
        return Response({
            "messesge": "Update Fail!"
        }, 400)

class UserRegister(APIView):

    def get(self, request):
        users = User.objects.all()
        # self.check_object_permissions(request, zone)
        serializer = s.AuthUserSerilaizer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serialized = s.CreateUserSerializer(data=data);
        if serialized.is_valid():
            serialized.save()
            new_user = dict(serialized.data)
            user_id = new_user.get('id')
            if user_id:
                profile = m.UserProfile(
                    account=data['account'],
                    birthday=data['birthday'],
                    nickname=data['account'],
                    user_id=user_id,
                )
                profile.save()
                return Response({
                            "status": 200,
                            "message": "Account register successfully!"
                        }, status=200)
            else :
                u = User.objects.get(id = user_id)
                u.delete()
                return Response(serialized._errors, status=400)    
        else: 
            return Response(serialized._errors, status=400)


        profile = m.UserProfile(
            account=data['account'],
            nickname=data['nickname'],
            birthday='2012-09-04 06:00Z',
            user_id=3,
        )
        profile.save()
        
        serializer = s.CreateProfileSerialzer(profile, many=True)
        return Response(serializer.data)
        # profile = s.CreateProfileSerialzer(data)
        return Response(serializer.data)



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
    def post(self, request, pk):
        # return Response(request.data)
        user = get_object_or_404(User, id=pk)
        data = request.data
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        # print(EMAIL_REGEX.match(data['email']))
        # print(m.Account.objects.all().filter(email=data['email']))
        if EMAIL_REGEX.match(data['email']):
            oldUser = m.Account.objects.filter(email=data['email'])
        else:
            oldUser = m.Family.objects.filter(email=data['email'])
        # print(oldUser)
        if (oldUser):
            return Response({
                "message": "Migrate Successfully!"
            })
        return Response({
            "message": "User infomation provide is incorrect!"
        }, 404)


class MigrateOldFamilyMember(APIView):
    def post(self, request, pk):
        return Response(request.data)
        user = get_object_or_404(User, id=pk)
        # self.check_object_permissions(request, zone)
        serializer = s.UserSerializer(user)
        return Response(serializer.data)
    # permission_classes = (IsAuthenticated,)
# def get(self, request):
#     # user = request.user
#     users = m.User.objects.all()
#     serializer = s.UserSerializer(users, many=True)
#     # return JsonResponse(serializer.data, safe=False)
#     return Response(serializer.data)
# @csrf_exempt
# def user_detail(request, pk):
#     """
#     User Detail
#     """
#     if request.method == 'GET':
#         try:
#             user = User.objects.filter(pk=pk)
#         except User.DoesNotExist:
#             return HttpResponse(status=404)

#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def user_is_old_member(request, pk):
#     """
#     User Detail
#     """
#     if request.method == 'GET':
#         try:
#             user = User.objects.filter(pk=pk)
#         except User.DoesNotExist:
#             return HttpResponse(status=404)

#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def user_migrate_account(request, pk):
#     """
#     User Detail
#     """
#     if request.method == 'GET':
#         try:
#             user = User.objects.filter(pk=pk)
#         except User.DoesNotExist:
#             return HttpResponse(status=404)

#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)