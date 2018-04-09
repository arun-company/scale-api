from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
# from django.core.exceptions.standarderror import ValueError
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
from datetime import datetime
from django.db.models import Count, Avg, Max, Min

# import datetime as dtime
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
    permission_classes = (IsAuthenticated,)

    def get(self, request, account_id):
        # return Response({'account_id': account_id})
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        # self.check_object_permissions(request, zone)
        serializer = s.UPS(profile)
        return Response(serializer.data)
    def patch(self, request, account_id, format=None):
        data = request.data
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)

        if (profile):
            user_id = profile.user_id
            # username = data['username']
            if data.get('username'):
                m.UserProfile.objects.filter(id=profile.id).update(name=data['username'])
            if data.get('birthday'):
                m.UserProfile.objects.filter(id=profile.id).update(birthday=data.get('birthday'))
            if data.get('gender'):
                m.UserProfile.objects.filter(id=profile.id).update(gender=data.get('gender'))
            if data.get('height'):
                m.UserProfile.objects.filter(id=profile.id).update(height=data.get('height'))
            if data.get('state'):
                m.UserProfile.objects.filter(id=profile.id).update(state=data.get('state'))
            
            return Response({
                "result": True
            })

        serializer = s.UPS(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, account_id):
        # user = get_object_or_404(User, id=pk)
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)
        if profile.delete():
            return Response({
                "result": True
            }, 200)
        return Response({
            "result": False
        }, 400)

class UserResetPassword(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, account_id):
        # return Response({'account_id': account_id})
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)
        # self.check_object_permissions(request, zone)
        serializer = s.UPS(profile)
        return Response(serializer.data)
    def patch(self, request, account_id, format=None):
        data = request.data
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)

        if (profile):
            user_id = profile.user_id
            user = get_object_or_404(m.User, id=user_id)
            if data.get('password'):
                user.set_password(data.get('password'))
                user.save()
            
            return Response({
                "result": True
            })
        return Response({
                "result": False
            }, 202)

    def delete(self, request, account_id):
        # user = get_object_or_404(User, id=pk)
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)
        if profile.delete():
            return Response({
                "result": True
            }, 200)
        return Response({
            "result": False
        }, 400)


class UserRegister(APIView):
    def post(self, request):
        data = request.data
        serialized = s.CreateUserSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            new_user = dict(serialized.data)
            user_id = new_user.get('id')
            if user_id:
                profile = m.UserProfile (
                    user_id=user_id
                )
                profile.birthday = data.get('birthday')
                profile.gender = data.get('gender') if data.get('gender') else 0
                profile.height = data.get('height') if data.get('height') else 0
                profile.name = data.get('username')
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
        
class UserSignin(APIView):
    def post(self, request):
        return Response({
            "Result": "Not Allow!"
        }, 500)
        serializer = s.TokenSerializer(request.data)
        serializer.is_valid(raise_exception=True)



class ExistingMember(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, pk):
        data = request.data
        try:
            member = get_object_or_404(m.Account, email=data['email'])
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Member email not found.'
            }, 202)

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

class MigrationOldAccounts(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, account_id):
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "accountConfirmed": 'False',
                "message": 'Account id incorrect.'
            }, 202)
        
        data = request.data

        health_email = data.get('health_email')
        health_password = data.get('health_password')
        healthplus_email = data.get('healthplus_email')
        healthplus_password = data.get('healthplus_password')
        healthAccount = m.Account.objects.filter(email=health_email, password=health_password)
        health= False
        if (healthAccount):
            health= True
            m.Weight.objects.filter(account_id=healthAccount[0].acc_id).update(account_id=profile.account_id, legacy=0)
            m.Account.objects.filter(email=health_email, password=health_password).delete()
        healthplus_member = m.Family.objects.filter(email=healthplus_email, password=healthplus_password)
        if (healthplus_member):
            family_no = healthplus_member[0].family_no
            allProfile = m.Profile.objects.filter(family_no=family_no)
            serializer = s.FamilyProfileSerializer(allProfile, many=True)
            return Response({
                "accountConfirmed": True,
                "accountType": 2,
                "familyMembers": serializer.data
            })
        if health:
            return Response({
                "accountConfirmed": True,
                "accountType": 1,
                "familyMembers": {}
                })    
        return Response({
            "accountConfirmed": 'False',
        }, 202)

class MigrateOldAccount(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, account_id):
        # return Response(request.data)
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "accountConfirmed": 'False',
                "message": 'Account id incorrect.'
            }, 400)
        data = request.data
        # return Response(data)
        health_email = data.get('health_email')
        health_password = data.get('health_password')
        healthplus_email = data.get('healthplus_email')
        healthplus_password = data.get('healthplus_password')

        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        if EMAIL_REGEX.match(data['email']):
            oldUser = m.Account.objects.filter(email=data['email'], password=data['password'])
            if (oldUser):
                serializer = s.AccountSerializer(oldUser, many=True)
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
    permission_classes = (IsAuthenticated,)
    def post(self, request, account_id):
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 400)
        data = request.data
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        if EMAIL_REGEX.match(data['family_email']):
            oldUser = m.Account.objects.filter(email=data['family_email'], password=data['family_password'])
            if (oldUser):
                serializer = s.AccountSerializer(oldUser, many=True)
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
        return Response({
                    "familyMemberConfirmed": False,
                }, 202)

class Weight(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, account_id):
        data = request.query_params
        date = data.get('date')
        if date:
            try:
                minDate = datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                return Response({
                    "result": 'False',
                    "message": 'Date format is incorrect.'
                }, 400)
            maxDate = datetime(minDate.year, minDate.month, minDate.day, 23, 59, 59)
            weight = m.Weight.objects.filter(measured__gte=minDate,
                                    measured__lte=maxDate, account_id=account_id)
            serializer = s.WeightSerializer(weight, many=True)
            return Response(serializer.data)
        elif data.get('month'):
            date = data.get('month')
            try:
                newDate = datetime.strptime(date, '%Y-%m')
            except ValueError:
                return Response({
                    "result": 'False',
                    "message": 'Date format is incorrect.'
                }, 400)
           
            minDate = datetime(newDate.year, newDate.month, 1, 0, 0,0)
            maxDate = datetime(newDate.year, newDate.month+1, 1)
            weight = m.Weight.objects.filter(measured__gte=minDate,
                                    measured__lt=maxDate, account_id=account_id)
            serializer = s.WeightSerializer(weight, many=True)
            return Response(serializer.data)
        elif data.get('year'):
            date = data.get('year')
            try:
                newDate = datetime.strptime(date, '%Y')
            except ValueError:
                return Response({
                    "result": 'False',
                    "message": 'Date format is incorrect.'
                }, 400)
            minDate = datetime(newDate.year, 1, 1, 0, 0,0)
            maxDate = datetime(newDate.year+1, 1, 1)
            weight = m.Weight.objects.filter(measured__gte=minDate,
                                    measured__lt=maxDate, account_id=account_id)
            serializer = s.WeightSerializer(weight, many=True)
            return Response(serializer.data)
        profile = get_object_or_404(m.UserProfile, account_id=account_id)
        print(request)
        return Response(data)
    
    def put(self, request, account_id):
        data = request.data.get('datas')
        weight = False
        if not data: 
            return Response({
                    'result': False,
                    'message': 'Datas have to be array.'
                }, 400)
        try:
            profile = get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": False,
                "message": "Account Id not found."
            }, 400)
    
        try:
           arrayWeights = json.loads(data)
           for weightData in arrayWeights:
               if not weightData.get('weight') or not weightData.get('measured'):
                   return Response({
                        "result": False,
                        "message": "weight and measured can not be null."
                    }, 400)
               weight =  m.Weight.objects.create(
                            account_id=account_id,
                            weight=weightData.get('weight'),
                            BMI=weightData.get('BMI'),
                            BFR=weightData.get('BFR'),
                            BWR=weightData.get('BWR'),
                            MMR=weightData.get('MMR'),
                            BD=weightData.get('BD'),
                            measured= weightData.get('measured'),
                            legacy=0
                        )
        except ValidationError:
            return Response({
                "result": False,
                "message": "Input Fields incorrect."
            }, 400)
        except Exception:
            return Response({
                "result": False,
                "message": "Json datas are incorrect."
            }, 400)
            
        if weight:
            return Response({
                'result': True
            })
        return Response({
            'result': False
        })
    def delete(self, request, account_id):
        data = request.query_params
        try:
            get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 400)
        wIds = data.get('ids').split(',')
        # serial = s.WeightSerializer(m.Weight.objects.filter(id__in=wIds,account_id=account_id), many=True)
        # return Response({
        #     'result': serial.data
        # })
        if len(m.Weight.objects.filter(id__in=wIds, account_id=account_id)):
            m.Weight.objects.filter(id__in=wIds, account_id=account_id).delete()
            return Response({
                'result': True
            },204)
        return Response({
                'result': False
            }, 202)


class AverageWeight(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, account_id):
        data = request.query_params
        if data.get('month'):
            date = data.get('month')
            try:
                newDate = datetime.strptime(date, '%Y-%m')
            except ValueError:
                return Response({
                    "result": 'False',
                    "message": 'Date format is incorrect.'
                }, 400)
            minDate = datetime(newDate.year, newDate.month, 1, 0, 0,0)
            maxDate = datetime(newDate.year, newDate.month+1, 1)
            weight = m.Weight.objects.filter(measured__gte=minDate, measured__lt=maxDate, account_id=account_id).extra({'filtertime' : "date(measured)"}).values("filtertime").annotate(
                total=Count('id'),
                day=Max('measured'), 
                averageWeight=Avg('weight'), 
                minWeight=Min('weight'),
                maxWeight=Max('weight'),
                averageBMI=Avg('BMI'),
                averageBFR=Avg('BFR'),
                averageBWR=Avg('BWR'),
                averageMMR=Avg('MMR'),
                averageBD=Avg('BD'),
                ).order_by('day')
            serializer = s.AverageWeightSerializer(weight, many=True)
            return Response(serializer.data)
        elif data.get('year'):
            date = data.get('year')
            try:
                newDate = datetime.strptime(date, '%Y')
            except ValueError:
                return Response({
                    "result": 'False',
                    "message": 'Date format is incorrect.'
                }, 400)
            minDate = datetime(newDate.year, 1, 1, 0, 0,0)
            maxDate = datetime(newDate.year+1, 1, 1)
            weight = m.Weight.objects.filter(measured__gte=minDate, measured__lt=maxDate, account_id=account_id).extra({'filtertime' : "MONTH(DATE(measured))"}).values("filtertime").annotate(
                total=Count('id'),
                month=Max('measured'), 
                averageWeight=Avg('weight'), 
                minWeight=Min('weight'),
                maxWeight=Max('weight'),
                averageBMI=Avg('BMI'),
                averageBFR=Avg('BFR'),
                averageBWR=Avg('BWR'),
                averageMMR=Avg('MMR'),
                averageBD=Avg('BD'),
                ).order_by('month')
            print(weight)
            serializer = s.AverageWeightMonthlySerializer(weight, many=True)
            return Response(serializer.data)
        return Response({
                    "result": False,
                    "message": "An argument should be Month or Year."
                }, 400)


class WeightUnknown(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, account_id):
        data = request.query_params
        device_id = data.get('device_id')

        if device_id:
            weight_unknow = m.WeightUnknown.objects.filter(device_id=device_id)
            serializer = s.WeightUnknownSerializer(weight_unknow, many=True)
            return Response(serializer.data)
        return Response({
            "result": "missing device_id"
        })

    def put(self, request, account_id):
        data = request.data.get('datas')
        weight = False
        if not data: 
            return Response({
                    'result': False,
                    'message': 'Datas have to be array.'
                }, 400)
        try:
            get_object_or_404(m.UserProfile, account_id=account_id)
            arrayWeights = json.loads(data)

            for weightData in arrayWeights:
                if not weightData.get('weight') or not weightData.get('measured'):
                    return Response({
                        "result": False,
                        "message": "weight and measured can not be null."
                    }, 400)
                weight =  m.WeightUnknown.objects.create(
                    account_id=account_id,
                    device_id=weightData.get('device_id'),
                    weight=weightData.get('weight'),
                    BMI=weightData.get('BMI'),
                    BFR=weightData.get('BFR'),
                    BWR=weightData.get('BWR'),
                    MMR=weightData.get('MMR'),
                    BD=weightData.get('BD'),
                    measured=weightData.get('measured'),
                    legacy=0
                )
        except ValidationError:
            return Response({
                "result": 'False',
                "message": "Input fields incorrect."
            }, 400)
        except Exception:
            return Response({
                "result": False,
                "message": "Json format are incorrect."
            }, 400)
        
        if weight:
            return Response({
                'result': True
            },201)
        return Response({
            'result': False
        },400)
    def delete(self, request, account_id):
        data = request.query_params
        try:
            get_object_or_404(m.UserProfile, account_id=account_id)
        except ValidationError:
            return Response({
                "result": 'False',
                "message": 'Account id incorrect.'
            }, 202)
        wIds = data.get('ids').split(',')
        # serial = s.WeightUnknownSerializer(m.WeightUnknown.objects.filter(id__in=wIds), many=True)
        # return Response({
        #     'result': serial.data
        # })
        if len(m.WeightUnknown.objects.filter(id__in=wIds)):
            m.WeightUnknown.objects.filter(id__in=wIds).delete()
            return Response({
                'result': True
            }, 204)
        return Response({
                'result': False
            },202)