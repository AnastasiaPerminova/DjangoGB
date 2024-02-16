from random import randint, choice

from django.core.management.base import BaseCommand
from homework_app.models import Customer, Product, Order
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        customers = Customer.objects.all()
        products = Product.objects.all()

        for customer in customers:
            for _ in range(randint(1, 3)):
                order = Order(
                    customer=customer
                )
                order.save()
                for _ in range(randint(1, 5)):
                    order.product.add(choice(products))

                order.save()

                ordered_products = order.product.all()
                total_price = 0
                for product in ordered_products:
                    total_price += product.price

                order.total_price = total_price
                order.save()

