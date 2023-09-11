from django.http import HttpResponse
from .models import Customer, Product, Order
from .management.commands.create_customer import Command as CustomerCommand
from .management.commands.create_product import Command as ProductCommand
from .management.commands.create_order import Command as OrderCommand

import logging

logger = logging.getLogger(__name__)


def create_customer(request):
    logger.info('Customer creation has been requested.')
    create_customer_command = CustomerCommand()
    create_customer_command.handle()
    latest_customer = Customer.objects.latest('id')
    result = (f'New customer has been registered:<br>'
              f'{latest_customer.name},<br>'
              f'{latest_customer.email},<br>'
              f'{latest_customer.phone},<br>'
              f'{latest_customer.address},<br>'
              f'{latest_customer.registered}')
    # return HttpResponse(latest_customer)  # try it?
    return HttpResponse(result)


def get_customers(request):
    logger.info('Customers list has been requested.')
    result = '<br>'.join(str(i) for i in Customer.objects.all())
    return HttpResponse(result)


def get_customer(request):
    pass


def create_product(request):
    logger.info('Product creation has been requested.')
    create_product_command = ProductCommand()
    create_product_command.handle()
    latest_product = Product.objects.latest('id')
    result = (f'New product has been successfully added:<br>'
              f'{latest_product.title},<br>'
              f'{latest_product.description},<br>'
              f'{latest_product.price},<br>'
              f'{latest_product.quantity},<br>'
              f'{latest_product.added}')
    # return HttpResponse(latest_product)  # try it?
    return HttpResponse(result)


def get_products(request):
    result = '<br>'.join(str(i) for i in Product.objects.all())
    return HttpResponse(result)


def get_product(request):
    pass


def create_order(request):
    create_order_command = OrderCommand()
    create_order_command.handle()
    latest_order = Order.objects.latest('id')
    result = (f'New order has been placed:<br>'
              f'{latest_order}')
    return HttpResponse(result)


def get_orders(request):
    result = '<br>'.join(str(i) for i in Order.objects.all())
    return HttpResponse(result)


def get_order(request):
    pass


def customer_min_orders(request):
    pass


def customer_max_orders(request):
    pass


def product_price_gt(request):
    pass


def product_price_lt(request):
    pass


def product_price_exact(request):
    pass


def get_orders_from(request):
    pass


def get_orders_placed_at(request):
    pass
