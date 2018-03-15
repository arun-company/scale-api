from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^1.0/users/$', views.user_list),
    url(r'^1.0/users/(?P<pk>[0-9]+)/detail$', views.user_detail),
    url(r'^1.0/users/(?P<pk>[0-9]+)/isOldMember$', views.user_detail),
    url(r'^1.0/users/(?P<pk>[0-9]+)/migrateOldAccount$', views.user_migrate_account),
]