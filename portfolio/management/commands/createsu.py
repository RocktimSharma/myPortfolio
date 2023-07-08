# images/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import environ

env=environ.Env()
environ.Env.read_env()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=env('ADMIN_USERNAME'),
                password=env('ADMIN_PASSWORD')
            )
