from django.core.management.base import BaseCommand
from watchman.factories import UserFactory


class Command(BaseCommand):
    help = 'Adds dummy user data to the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int)

    def handle(self, *args, **options):
        number_of_users = options['number_of_users']
        UserFactory.create_batch(number_of_users)
