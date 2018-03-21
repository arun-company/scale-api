from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^user/register$', views.UserRegister.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/detail$', views.UserDetail.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/isOldMember$', views.ExistingMember.as_view()),
#     url(r'^1.0/users/(?P<pk>[0-9]+)/migrateOldAccount$', views.user_migrate_account),
]