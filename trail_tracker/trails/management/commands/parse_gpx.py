import json, xmltodict

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help ="""
        Accepts GPX file and converts to JSON object

        Needs more robust error handling and validation.
        """

    def add_arguments(self, parser):
        parser.add_argument('gpx_file', type=file)

    def handle(self, *args, **options):
        for gpx_file in options['gpx_file']:
            try:
                gpx = open(gpx_file, 'r')
                ride_dict = xmltodict.parse(gpx, xml_attribs=True)
                return json.dumps(ride_dict, indent=4)
