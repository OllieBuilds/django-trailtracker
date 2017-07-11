# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from rest_framework import viewsets
from trail_tracker.api.serializers import TrailSerializer

from trail_tracker.trails.models import Trail

class ListTrailsViewSet(viewsets.ModelViewSet):
    model = Trail
    # queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'name'

    def get_queryset(self):
        query = Trail.objects.all()

        print self.request
        return query
