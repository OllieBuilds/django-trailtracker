from rest_framework import serializers
from trail_tracker.trails.models import Trail


class TrailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Trail
        fields = ['name', 'city', 'state', 'country', 'lat', 'lon']

        
