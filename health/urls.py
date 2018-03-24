from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^user/(?P<account_id>[0-9a-f]*)/profile$', views.UserInfo.as_view()),
    url(r'^user/(?P<account_id>[0-9a-zA-z]*)$', views.UserInfo.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/isOldMember$', views.ExistingMember.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/migrateOldAccount$', views.MigrateOldAccount.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/migrateOldFamilyMember$', views.MigrateOldFamilyMember.as_view()),
    url(r'^auth/registration$', views.UserRegister.as_view()),
    url(r'^auth/signin$', views.UserRegister.as_view()),
#     url(r'^1.0/users/(?P<pk>[0-9]+)/migrateOldAccount$', views.user_migrate_account),
]