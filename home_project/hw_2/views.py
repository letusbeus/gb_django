from django.http import HttpResponse
from .models import Customer, Product, Order
from .management.commands.create_customer import Command


def create_customer(request):
    create_customer_command = Command()
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
    result = '<br>'.join(str(i) for i in Customer.objects.all())
    return HttpResponse(result)


def get_customer(request):
    pass


def get_products(request):
    result = '<br>'.join(str(i) for i in Product.objects.all())
    return HttpResponse(result)


def get_product(request):
    pass


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
