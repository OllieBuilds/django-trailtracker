from django.conf.urls import url
from trail_tracker.trails.views import ListTrailsView

urlpatterns = [
    url(r'^trails', ListTrailsView.as_view(), name='trails'),
]
