# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from trail_tracker.trails.models import Trail

class TestClass(ListView):
    model = Trail
    template_name = 'trails/trails_list.html'

    def render_to_response(self, request):
        print(self)
        return super(TestClass, self).render_to_response(request)
