from random import randint
from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Create fake product.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        counter = kwargs.get('counter')
        for i in range(1, counter + 1):
            product = Product(
                name=f'Customer{i}',
                email=f'customer{i}@mail.ru',
                phone=f'8{randint(9000000000, 9999999999)}',
                address=f'address{i}',
                registered=f'{randint(2020, 2023)}-{randint(1, 12)}-{randint(1, 31)}'

            )
            product.save()

