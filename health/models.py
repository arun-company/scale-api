from django.db import models
from django.contrib.auth.models import User
import uuid


# Health APP
class Account(models.Model):
    app = models.CharField(max_length=32, blank=True,default=None,null=True)
    acc_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    carrier = models.CharField(max_length=50, blank=True,default=None,null=True)
    username = models.CharField(max_length=50, blank=True,default=None,null=True)
    password = models.CharField(max_length=255, blank=True,default=None,null=True)
    email = models.CharField(max_length=127, blank=True,default=None,null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=127, blank=True,default=None,null=True)
    homedir = models.CharField(max_length=255, blank=True,default=None,null=True)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'health_account'
        ordering = ('created',)

# Health APP
class AccountProfile(models.Model):
    profile_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    name = models.CharField(max_length=50, blank=True,default=None,null=True)
    value = models.CharField(max_length=255, blank=True,default=None,null=True)
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'health_account_profile'
        ordering = ('created',)
# Health APP
class Member(models.Model):
    member_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    name = models.CharField(max_length=50, blank=True,default=None,null=True)
    birthday = models.DateTimeField()
    sex = models.IntegerField()
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'health_member'
        ordering = ('created',)


# Health Plus APP
class Family(models.Model):
    family_no = models.AutoField(primary_key=True)
    family_id = models.CharField(max_length=50, blank=True,default=None,null=True)
    email = models.CharField(max_length=127, blank=True,default=None,null=True)
    password = models.CharField(max_length=255, blank=True,default=None,null=True)
    family_name = models.CharField(max_length=50, blank=True,default=None,null=True)
    image = models.CharField(max_length=255, blank=True,default=None,null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'healthplus_family'
        ordering = ('created',)

# Health Plus APP
class FamilyWeight(models.Model):
    seq = models.AutoField(primary_key=True)
    profile_id = models.IntegerField()
    family_no = models.IntegerField()
    weight = models.FloatField()
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'healthplus_family_weight'
        ordering = ('created',)

# Health Plus APP
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    family_no = models.IntegerField()
    nickname = models.CharField(max_length=100, blank=True,default=None,null=True)
    birth = models.IntegerField()
    gender = models.SmallIntegerField(default=1)
    height = models.FloatField(default=None,null=True)
    image = models.CharField(max_length=255)
    secret = models.CharField(max_length=127, blank=True,default=None,null=True)
    secret_email = models.CharField(max_length=127, blank=True,default=None,null=True)
    secret_pw = models.CharField(max_length=127, blank=True,default=None,null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'healthplus_profile'
        ordering = ('created',)

class Weight(models.Model):
    account_id = models.CharField(max_length=100, blank=True,default=None,null=True)
    weight = models.FloatField(blank=True,default=None,null=True)
    BMI = models.FloatField(blank=True,default=None,null=True)
    BFR = models.FloatField(blank=True,default=None,null=True)
    BWR = models.FloatField(blank=True,default=None,null=True)
    MMR = models.FloatField(blank=True,default=None,null=True)
    BD = models.FloatField(blank=True,default=None,null=True)
    legacy = models.SmallIntegerField()
    measured = models.DateTimeField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'weights'
        ordering = ('added',)
class UnknownWeight(models.Model):
    account_id = models.CharField(max_length=100, blank=True,default=None,null=True)
    weight = models.FloatField(blank=True,default=None,null=True)
    BMI = models.FloatField(blank=True,default=None,null=True)
    BFR = models.FloatField(blank=True,default=None,null=True)
    BWR = models.FloatField(blank=True,default=None,null=True)
    MMR = models.FloatField(blank=True,default=None,null=True)
    BD = models.FloatField(blank=True,default=None,null=True)
    legacy = models.SmallIntegerField()
    measured = models.DateTimeField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=12, blank=True,default=None,null=True)
    device_sn = models.CharField(max_length=16, blank=True,default=None,null=True)
    class Meta:
        db_table = 'unknowweights'
        ordering = ('added', 'measured')

# Health APP
class WeightRecord(models.Model):
    weight_record_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    member_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    device_id = models.CharField(max_length=12, blank=True,default=None,null=True)
    device_sn = models.CharField(max_length=16, blank=True,default=None,null=True)
    measurement_date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    bmi = models.FloatField()
    pbf = models.FloatField()
    wt_state = models.IntegerField()
    resistance = models.IntegerField()
    body_water = models.FloatField()
    muscle = models.FloatField()
    bone = models.FloatField()
    remark = models.CharField(max_length=255, blank=True,default=None,null=True)
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    utc = models.CharField(max_length=255, blank=True,default=None,null=True)
    userNo = models.IntegerField()
    pbf_state = models.IntegerField()
    basalMetabolism = models.FloatField()
    visceralFatLevel = models.FloatField()
    
    class Meta:
        db_table = 'health_weight_record'
        ordering = ('created',)  

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    # username = models.CharField(max_length=100, blank=True,default=None,null=True)
    # password = models.CharField(max_length=255, blank=True,default=None,null=True)
    # email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True,default=None,null=True)
    birthday = models.DateTimeField(default=None, blank=True, null=True)
    gender = models.SmallIntegerField(default=1)
    height = models.IntegerField(default=None, blank=True, null=True)
    image = models.CharField(max_length=255)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_profile'
        ordering = ('created',)
