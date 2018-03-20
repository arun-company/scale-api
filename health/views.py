from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from health import models as m
from django.views.decorators.csrf import csrf_exempt
from health import serializers as s

class UserViewList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = m.User.objects.all().order_by('created')
    serializer_class = s.UserSerializer

class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # user = request.user
        users = m.User.objects.all()
        serializer = s.UserSerializer(users, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

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