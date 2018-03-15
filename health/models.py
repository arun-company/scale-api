from django.db import models

class User(models.Model):
    account = models.CharField(max_length=100, blank=True, default='')
    username = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=255, blank=True, default='')
    email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(blank=True)
    gender = models.SmallIntegerField(default=1)
    height = models.IntegerField()
    image = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ('created',)

class Account(models.Model):
    app = models.CharField(max_length=32, blank=True, default='')
    carrier = models.CharField(max_length=50, blank=True, default='')
    username = models.CharField(max_length=50, blank=True, default='')
    password = models.CharField(max_length=255, blank=True, default='')
    email = models.CharField(max_length=127, blank=True, default='')
    mobile = models.CharField(max_length=11, blank=True, default='')
    name = models.CharField(max_length=127, blank=True, default='')
    homedir = models.CharField(max_length=255, blank=True, default='')
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'account'
        ordering = ('created',)

class AccountProfile(models.Model):
    account_id = models.CharField(max_length=32, blank=True, default='')
    name = models.CharField(max_length=50, blank=True, default='')
    value = models.CharField(max_length=255, blank=True, default='')
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'account_profile'
        ordering = ('created',)

class Member(models.Model):
    account_id = models.CharField(max_length=32, blank=True, default='')
    name = models.CharField(max_length=50, blank=True, default='')
    birthday = models.DateTimeField()
    sex = models.IntegerField()
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'member'
        ordering = ('created',)


class Family(models.Model):
    family_no = models.AutoField(primary_key=True)
    family_id = models.CharField(max_length=50, blank=True, default='')
    email = models.CharField(max_length=127, blank=True, default='')
    password = models.CharField(max_length=255, blank=True, default='')
    family_name = models.CharField(max_length=50, blank=True, default='')
    image = models.CharField(max_length=255, blank=True, default='')
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'family'
        ordering = ('created',)

class FamilyWeight(models.Model):
    seq = models.AutoField(primary_key=True)
    profile_id = models.IntegerField()
    family_no = models.IntegerField()
    weight = models.FloatField()
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'family_weight'
        ordering = ('created',)

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    family_no = models.IntegerField()
    nickname = models.CharField(max_length=100, blank=True, default='')
    birth = models.IntegerField()
    gender = models.SmallIntegerField(default=1)
    height = models.IntegerField()
    image = models.CharField(max_length=255)
    secret = models.CharField(max_length=127, blank=True, default='')
    secret_email = models.CharField(max_length=127, blank=True, default='')
    secret_pw = models.CharField(max_length=127, blank=True, default='')
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'profile'
        ordering = ('created',)  

class Weight(models.Model):
    account = models.CharField(max_length=100, blank=True, default='')
    weight = models.FloatField()
    BMI = models.FloatField()
    BFR = models.FloatField()
    MMR = models.FloatField()
    BD = models.FloatField()
    legacy = models.SmallIntegerField()
    mearsured = models.DateTimeField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'weight'
        ordering = ('added',)

class WeightRecord(models.Model):

    account_id = models.CharField(max_length=32, blank=True, default='')
    member_id = models.CharField(max_length=32, blank=True, default='')
    device_id = models.CharField(max_length=12, blank=True, default='')
    device_sn = models.CharField(max_length=16, blank=True, default='')
    measurement_date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    bmi = models.FloatField()
    pbf = models.FloatField()
    wt_state = models.IntegerField()
    resistance = models.IntegerField()
    body_water = models.FloatField()
    muscle = models.FloatField()
    bone = models.FloatField()
    remark = models.CharField(max_length=255, blank=True, default='')
    deleted = models.BooleanField(default=False)
    ts = models.BigIntegerField(blank=True)
    client_id = models.CharField(max_length=32, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    utc = models.CharField(max_length=255, blank=True, default='')
    userNo = models.IntegerField()
    pbf_state = models.IntegerField()
    basalMetabolism = models.FloatField()
    visceralFatLevel = models.FloatField()
    
    class Meta:
        db_table = 'weight_record'
        ordering = ('created',)  
