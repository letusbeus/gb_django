from random import randint
from django.core.management.base import BaseCommand
from home_project.hw_2.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **kwargs):
        i = Product.objects.count() + 1
        product = Product(
            title=f'Product_{i}',
            description=f'Product_description_{i}',
            price=f'{randint(0, 9999) / 10}',
            quantity=f'{randint(0, 99)}',
            added=f'{randint(2020, 2023)}-{randint(1, 12)}-{randint(1, 31)}'
        )
        print(f'New product has been successfully added:\n{product}')
        product.save()
