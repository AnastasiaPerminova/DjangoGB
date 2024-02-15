from decimal import Decimal

from django.core.management.base import BaseCommand
from homework_app.models import Product


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=Decimal, help='Prodcut prie')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(name=name, description=description,
                            price=price, quantity=quantity)
        product.save()
        self.stdout.write(f'{product}')
