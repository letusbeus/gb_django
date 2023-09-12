from random import randint

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from .my_command import generate_random_date
from hw_2.models import Customer


class Command(BaseCommand):
    help = 'Create customer.'

    def handle(self, *args, **kwargs):
        try:
            i = Customer.objects.latest('id').id + 1
        except ObjectDoesNotExist:
            i = 1
        customer = Customer(
            name=f'Customer{i}',
            email=f'customer{i}@mail.ru',
            phone=f'8{randint(9000000000, 9999999999)}',
            address=f'address{i}',
            registered=f'{generate_random_date(2010, 2022)}'
        )
        customer.save()
        self.stdout.write(f'New customer has been successfully registered:\n{customer}')
