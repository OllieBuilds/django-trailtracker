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

    question = StringField(max_length=200)
    # CharField(_('name'), max_length=settings.TRAIL_NAME_MAX_LENGTH, default='')
    # CharField(_('city'), max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='')
    # CharField(_('state'), max_length=2, default='')
    # CharField(_('country'), max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='US')

    # GPS location of trailhead
    # FloatField(_('latitude'), default='')
    # FloatField(_('longitude'), default='')

    @classmethod
    def create(cls, name='test', city='Boston', state='MA',
                    country='US', lat=123, lon=321):

        trail = cls(name=name, city=city, state=state, country=country, lat=lat, lon=lon)
        return trail
