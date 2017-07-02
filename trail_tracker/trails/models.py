# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Trail(models.Model):
    """
    Trail model references IRL trails
    """

    name = models.CharField(_('name'), max_length=settings.TRAIL_NAME_MAX_LENGTH, default='')
    city = models.CharField(_('city'), max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='')
    state = models.CharField(_('state'), max_length=2, default='')
    country = models.CharField(_('country'), max_length=settings.DEFAULT_MODEL_FIELD_LENGTH, default='US')

    # GPS location of trailhead
    lat = models.FloatField(_('latitude'), default='')
    lon = models.FloatField(_('longitude'), default='')

    @classmethod
    def create(cls, name='test', city='Boston', state='MA',
                    country='US', lat=123, lon=321):

        trail = cls(name=name, city=city, state=state, country=country, lat=lat, lon=lon)
        return trail
