from django.core.management.base import BaseCommand
from watchman.factories import RecordFactory


class Command(BaseCommand):
    help = 'Adds dummy user records from random users to the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int)

    def handle(self, *args, **options):
        number_of_records = options['number_of_records']

        for _ in range(number_of_records):
            record = RecordFactory()
            record.save()
