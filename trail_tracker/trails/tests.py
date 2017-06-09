# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.test import TestCase
from trail_tracker.trails.models import Trail

class TestModel(unittest.TestCase):

    def test_orm_working(self):
        # Assumes database is empty
        trail = Trail.objects.all()
        self.assertEqual(len(trail), 0)

        # Create a sample Trail object
        trail = Trail(name="Test", city="Boston", state="MA")
        self.assertEqual(trail.name, "Test")
