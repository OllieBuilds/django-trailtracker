# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.shortcuts import render
from django.urls import reverse

from trail_tracker.trails.models import Trail
from django.views.generic import CreateView, ListView

# class CreateTrailView(CreateView):

class ListTrailsView(ListView):
    model= Trail
    template_name= 'trails/trails_list.html'

    def render_to_response(self, request):
        print dir(self)
        return super(ListTrailsView, self).render_to_response(self, request )
