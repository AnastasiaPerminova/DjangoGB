from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField(max_length=12)
    address = models.CharField(max_length=400)
    registration_date = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'{self.pk} - {self.name} - {self.email} - {self.phone} - {self.address}'

    def __str__(self):
        return f'{self.name} - {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    addition_date = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'{self.pk} - {self.name} - {self.description} - {self.price} - {self.quantity}'

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, default=None)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.customer} - {self.product.all()}'
