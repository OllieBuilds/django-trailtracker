from django.conf.urls import url, include
from trail_tracker.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'trails', views.TestClass, base_name='trails')

app_name = 'api'
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include(router.urls)),
]
