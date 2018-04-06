from django.contrib import admin

from health import models

admin.site.site_header = "Casapi Admin"

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','member_id', 'account_id','name','birthday','sex','deleted','ts', 'client_id', 'created')

admin.site.register(models.Member, MemberAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','app', 'acc_id','carrier','username','password','email','mobile', 'client_id', 'name')
   
admin.site.register(models.Account, AccountAdmin )

class FamilyWeightAdmin(admin.ModelAdmin):
    list_display = ('seq','profile_id', 'family_no','weight','state','created','updated')
   
admin.site.register(models.FamilyWeight, FamilyWeightAdmin )

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_no','family_id', 'email','password','family_name','image','updated')
admin.site.register(models.Family, FamilyAdmin )



class WeightAdmin(admin.ModelAdmin):
    list_display = ('id','account_id', 'weight','BMI','BFR','BWR','MMR','BD','legacy', 'measured')

admin.site.register(models.Weight, WeightAdmin )

class WeightUnknownAdmin(admin.ModelAdmin):
    list_display = ('id','account_id', 'device_id','weight','BMI','BFR','BWR','MMR','BD','legacy', 'measured')

admin.site.register(models.WeightUnknown, WeightUnknownAdmin )