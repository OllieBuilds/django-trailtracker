import json, xmltodict

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help ="""
        Accepts GPX file and converts to JSON object

        Needs more robust error handling and validation.
        """

    def add_arguments(self, parser):
        parser.add_argument('gpx_file', type=str)

    def handle(self, *args, **options):
            try:
                if options['gpx_file']:
                    gpx_file = options['gpx_file']

                with open(gpx_file, 'r') as gpx:
                    ride_dict = xmltodict.parse(gpx.read(), xml_attribs=True)
                    return json.dumps(ride_dict, indent=4)
            except:
                raise
