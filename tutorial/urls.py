from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from tutorial.quickstart import views as main_view
from health import views as health_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('health.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^password', include('health_aws_smtp.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

