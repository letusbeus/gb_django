from django.core.management.base import BaseCommand
from hw_2.models import Customer


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()  # get a list of all existing customers
        result = '\n'.join(f'{i + 1}. {customer}' for i, customer in enumerate(customers))  # convert to string
        self.stdout.write(f'{result}')  # display the result
