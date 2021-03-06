from django.db import models
from django.contrib.auth.models import User
import uuid


# Health APP
class Account(models.Model):
    app = models.CharField(max_length=255, blank=True,default=None,null=True)
    acc_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    carrier = models.CharField(max_length=50, blank=True,default=None,null=True)
    username = models.CharField(max_length=50, blank=True,default=None,null=True)
    password = models.CharField(max_length=255, blank=True,default=None,null=True)
    email = models.CharField(max_length=255, blank=True,default=None,null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True,default=None,null=True)
    homedir = models.CharField(max_length=255, blank=True,default=None,null=True)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'health_account'
        ordering = ('created',)

# Health APP
class AccountProfile(models.Model):
    profile_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    name = models.CharField(max_length=255, blank=True,default=None,null=True)
    value = models.CharField(max_length=255, blank=True,default=None,null=True)
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'health_account_profile'
        ordering = ('created',)
# Health APP
class Member(models.Model):
    member_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    name = models.CharField(max_length=255, blank=True,default=None,null=True)
    birthday = models.DateTimeField()
    sex = models.IntegerField()
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'health_member'
        ordering = ('created',)


# Health Plus APP
class Family(models.Model):
    family_no = models.AutoField(primary_key=True)
    family_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    email = models.CharField(max_length=255, blank=True,default=None,null=True)
    password = models.CharField(max_length=255, blank=True,default=None,null=True)
    family_name = models.CharField(max_length=255, blank=True,default=None,null=True)
    image = models.CharField(max_length=255, blank=True,default=None,null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'healthplus_family'
        ordering = ('created',)
        verbose_name = 'Familie'

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
    nickname = models.CharField(max_length=255, blank=True,default=None,null=True)
    birth = models.IntegerField()
    gender = models.SmallIntegerField(default=1)
    height = models.FloatField(default=None,null=True)
    image = models.CharField(max_length=255)
    secret = models.CharField(max_length=255, blank=True,default=None,null=True)
    secret_email = models.CharField(max_length=255, blank=True,default=None,null=True)
    secret_pw = models.CharField(max_length=255, blank=True,default=None,null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'healthplus_profile'
        ordering = ('created',)
        verbose_name = 'Member'

class Weight(models.Model):
    account_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    weight = models.FloatField(blank=True,default=None,null=True)
    BMI = models.FloatField(blank=True,default=0,null=True)
    BFR = models.FloatField(blank=True,default=0,null=True)
    BWR = models.FloatField(blank=True,default=0,null=True)
    MMR = models.FloatField(blank=True,default=0,null=True)
    BD = models.FloatField(blank=True,default=0,null=True)
    legacy = models.SmallIntegerField()
    measured = models.DateTimeField()
    added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'weights'
        ordering = ('added',)
class WeightUnknown(models.Model):
    account_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    weight = models.FloatField(blank=True,default=0,null=True)
    BMI = models.FloatField(blank=True,default=0,null=True)
    BFR = models.FloatField(blank=True,default=0,null=True)
    BWR = models.FloatField(blank=True,default=0,null=True)
    MMR = models.FloatField(blank=True,default=0,null=True)
    BD = models.FloatField(blank=True,default=0,null=True)
    legacy = models.SmallIntegerField()
    measured = models.DateTimeField()
    added = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    class Meta:
        db_table = 'weights_unknown'
        ordering = ('added', 'measured')

# Health APP
class WeightRecord(models.Model):
    weight_record_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    account_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    member_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    device_id = models.CharField(max_length=255, blank=True,default=None,null=True)
    device_sn = models.CharField(max_length=255, blank=True,default=None,null=True)
    measurement_date = models.DateTimeField()
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
    client_id = models.CharField(max_length=255, blank=True,default=None,null=True)
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
    name = models.CharField(max_length=255, blank=True,default=None,null=True)
    birthday = models.DateTimeField(default=None, blank=True, null=True)
    gender = models.SmallIntegerField(default=1)
    height = models.FloatField(default=0)
    image =  models.FileField(upload_to='profile/')
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_profile'
        ordering = ('created',)

class ResetPassword(models.Model):
    account_id = models.CharField(max_length=255)
    code =  models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'reset_password'
