# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
# from django.db import models
from mongoengine import *
from django.utils.translation import ugettext_lazy as _

class Trail(Document):
    """
    Trail model references IRL trails
    """

    name = StringField(max_length=settings.TRAIL_NAME_MAX_LENGTH, default='')
    city = StringField(max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='')
    state = StringField(max_length=2, default='')
    country = StringField(max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='US')

    # GPS location of trailhead
    lat = FloatField(default='')
    lon = FloatField(default='')

    @classmethod
    def create(cls, name='test', city='Boston', state='MA',
                    country='US', lat=123, lon=321):

        trail = cls(name=name, city=city, state=state, country=country, lat=lat, lon=lon)
        return trail
