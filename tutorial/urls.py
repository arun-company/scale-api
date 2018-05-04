from django.conf.urls import url, include
from rest_framework import routers
from health_aws_smtp import views as health_mail
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('health.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^auth', include('health_aws_smtp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

