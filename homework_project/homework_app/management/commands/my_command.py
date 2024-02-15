from django.core.management.base import BaseCommand
from homework_app.models import Customer, Product, Order


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            customer = Customer(name=f'name{i}',
                                email=f'user{i}@mail.com',
                                phone=f"+71111111{i}",
                                address=f'Address{i}')
            customer.save()

            product = Product(name=f'Product{i}',
                              description=f'Description{i}: bla bla bla...',
                              price=i * 100,
                              quantity=i
                              )
            product.save()





