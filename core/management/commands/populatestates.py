from django.core.management.base import BaseCommand
from core.models import CITIES, State


class Command(BaseCommand):
    """
    populates database with states
    """
    help = 'populates database with states'

    def handle(self, *args, **options):

        for ele_one, ele_two in CITIES:
            State.objects.create(name=ele_one)