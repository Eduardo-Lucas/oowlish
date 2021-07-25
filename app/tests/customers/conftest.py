import pytest

from customers.models import Customer


@pytest.fixture(scope='function')
def add_customer():
    def _add_customer(first_name, last_name, email, gender, company, city, title, latitude, longitude):
        customer = Customer.objects.create(first_name=first_name, last_name=last_name, email=email, gender=gender,
                                           company=company, city=city, title=title, latitude=latitude,
                                           longitude=longitude)
        return customer
    return _add_customer
