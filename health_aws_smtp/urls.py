from django.conf.urls import url
from health_aws_smtp import views

urlpatterns = [
    url(r'password-update/(?P<code>[0-9a-zA-z-]*)$', views.reset_password_form),
    url(r'password-hash', views.encrype_password),
#     url(r'^1.0/users/(?P<pk>[0-9]+)/migrateOldAccount$', views.user_migrate_account),
]
