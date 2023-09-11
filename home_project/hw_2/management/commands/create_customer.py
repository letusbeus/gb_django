from random import randint
from django.core.management.base import BaseCommand
from home_project.hw_2.models import Customer


class Command(BaseCommand):
    help = 'Create customer.'

    def handle(self, *args, **kwargs):
        i = Customer.objects.count() + 1
        customer = Customer(
            name=f'Customer{i}',
            email=f'customer{i}@mail.ru',
            phone=f'8{randint(9000000000, 9999999999)}',
            address=f'address{i}',
            registered=f'{randint(2020, 2023)}-{randint(1, 12)}-{randint(1, 31)}'
        )
        print(f'New customer has been successfully registered:\n{customer}')
        customer.save()
