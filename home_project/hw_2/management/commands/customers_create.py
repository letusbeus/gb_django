from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from .my_command import generate_random_date
from hw_2.models import Customer


class Command(BaseCommand):
    help = 'Create fake customers.'

    def add_arguments(self, parser):
        parser.add_argument('counter', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):

        try:
            last_customer_id = Customer.objects.latest('id').id + 1
        except ObjectDoesNotExist:
            last_customer_id = 1

        counter = kwargs.get('counter')
        for i in range(last_customer_id, last_customer_id + counter):
            customer = Customer(
                name=f'Customer{i}',
                email=f'customer{i}@mail.ru',
                phone=f'8{randint(9000000000, 9999999999)}',
                address=f'address{i}',
                registered=f'{generate_random_date(2010, 2022)}'
            )
            customer.save()
        self.stdout.write(f'{counter} new customer(s) has been successfully registered.')
