from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()  # get a list of all existing customers
        result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))  # convert to string
        self.stdout.write(f'{result}')  # display the result
