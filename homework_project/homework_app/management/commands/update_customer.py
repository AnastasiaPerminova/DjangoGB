from django.core.management.base import BaseCommand
from homework_app.models import Customer


class Command(BaseCommand):
    help = "Update customer email by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('email', type=str, help='Customer')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = kwargs.get('email')
        customer = Customer.objects.filter(pk=pk).first()
        customer.email= email
        customer.save()
        self.stdout.write(f'{customer}')
