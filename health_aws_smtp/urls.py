from django.conf.urls import url
from health_aws_smtp import views

urlpatterns = [
    url(r'reset/(?P<pk>[0-9a-f]+)$', views.current_datetime),
    # url(r'^auth/signin$', views.UserRegister.as_view()),
#     url(r'^1.0/users/(?P<pk>[0-9]+)/migrateOldAccount$', views.user_migrate_account),
]
