from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Get product with price exact <price>'

    def add_arguments(self, parser):
        parser.add_argument('price', type=float, help='Product price')

    def handle(self, *args, **kwargs):
        price = kwargs['price']
        product = Product.objects.filter(price__exact=price)
        result = '\n'.join(str(i) for i in product)
        self.stdout.write(f'{result}')
