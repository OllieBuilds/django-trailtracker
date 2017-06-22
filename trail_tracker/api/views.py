# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from rest_framework import viewsets
from trail_tracker.api.serializers import TrailSerializer

from trail_tracker.trails.models import Trail

class TestClass(viewsets.ModelViewSet):
    model = Trail
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
