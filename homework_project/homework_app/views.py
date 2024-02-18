from datetime import datetime, timedelta, date

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .form import ProductFormUpdate
from .models import Customer, Order, Product

logger = logging.getLogger(__name__)


# Create your views here.

def main(request):
    logger.info('Main page accessed')
    html = f'''<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8"/>
      <title>Main</title>
    </head>
    <body>
      <h1>Django. GeekBrains. Seminars. </h1>
      <h2>Homework_project.</h2>
    </body>
    </html>'''

    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    text = f'''<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8"/>
      <title>About</title>
    </head>
    <body>
      <h1>It's a page about my django homework_project. </h1>
      
      <p> I've just started to learn Django and homework_1 has been done.</p>
    </body>
    </html>'''
    return HttpResponse(text)


def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {'customer': customer,
               'orders': orders}
    return render(request, 'homework_app/customer_orders.html', context)


def order_full(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = order.product.all()
    return render(request, 'homework_app/order_full.html', {'order': order, 'products': products})


def customer_products(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    customer_products = {}
    for order in orders:
        products = order.product.all()
        for product in products:
            if customer_products.get(product):
                if customer_products[product] > order.order_date:
                    customer_products[product] = order.order_date
            customer_products[product] = order.order_date
    products_this_week = {}
    products_this_month = {}
    products_this_year = {}

    for key, value in customer_products.items():
        print(f"value={type(value)}")
        print(f"today = {type(date.today())}")
        timedelta = date.today() - value
        print(timedelta)
        if timedelta.days < 7:
            products_this_week[key] = value
        elif timedelta.days < 30:
            products_this_month[key] = value
        elif timedelta.days < 365:
            products_this_year[key] = value

    context = {'customer': customer,
               'pr_week': products_this_week,
               'pr_month': products_this_month,
               'pr_year': products_this_year
               }
    return render(request, 'homework_app/customer_products.html', context)


def update_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = ProductFormUpdate(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            if name:
                product.name = name
            if description:
                product.description = description
            if quantity:
                product.quantity = quantity
            if price:
                product.price = price
            if image:
                product.image = image
            product.save()

    else:
        form = ProductFormUpdate()

    return render(request, 'homework_app/update_product.html', {'form': form, 'product': product})



