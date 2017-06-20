from django.conf.urls import url
from trail_tracker.api.views import TestClass

urlpatterns = [
    url(r'^api', TestClass.as_view(), name='test')
]
