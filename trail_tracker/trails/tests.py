# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import mongoengine
from django.test import TestCase
from trail_tracker.trails.models import Trail


class TestModel(unittest.TestCase):

    def setUp(self):
        # Disconnect from the database connection that is started in Django settings
        mongoengine.connection.disconnect('default')

        # Alias must be 'default' because the models are set to use the default database.
        self.conn = mongoengine.connect('mongoenginetest', host='mongomock://localhost', alias='test')

    def tearDown(self):
        # There is a bug in Mongomock's drop_database() implementation so we
        # must manually delete data to be sure that everything is cleaned up.

        # Loop over each of our Mongo collections and delete the records.
        collections = [Trail]
        for collection in collections:
            collection.objects.delete()

        self.conn.drop_database('mongoenginetest')

    def test_orm_working(self):
        # Assumes database is empty
        trail = Trail.objects.all()
        self.assertEqual(len(trail), 0)

        # Create a sample Trail object
        trail = Trail(name="Test", city="Boston", state="MA")
        self.assertEqual(trail.name, "Test")
