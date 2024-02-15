from django.core.management.base import BaseCommand
from homework_app.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Customer name')
        parser.add_argument('email', type=str, help='Customer email')
        parser.add_argument('phone', type=str, help='Customer phone')
        parser.add_argument('address', type=str, help='Customer address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        customer = Customer(name=name, email=email,
                            phone=phone, address=address)
        customer.save()
        self.stdout.write(f'{customer}')
