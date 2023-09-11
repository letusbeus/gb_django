from random import randint

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **kwargs):
        try:
            i = Product.objects.latest('id').id + 1
        except ObjectDoesNotExist:
            i = 1
        # i = Product.objects.count() + 1 # было
        product = Product(
            title=f'Product_{i}',
            description=f'Product_description_{i}',
            price=f'{randint(10, 9999) / 100}',
            quantity=f'{randint(1, 99)}',
            added=f'{randint(2020, 2023)}-{randint(1, 12)}-{randint(1, 31)}'
        )
        product.save()
        self.stdout.write(f'New product has been successfully added:\n{product}')
