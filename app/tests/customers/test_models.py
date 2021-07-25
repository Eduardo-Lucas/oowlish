import pytest

from customers.models import Customer


@pytest.mark.django_db
def test_customer_model():
    customer = Customer(first_name="Laura", last_name="Richards", email="lrichards0@reverbnation.com",
                        gender="Female", company="Meezzy", city="Warner, NH", title="Biostatistician III")
    customer.save()
    assert customer.first_name == "Laura"
    assert customer.last_name == "Richards"
    assert customer.email == "lrichards0@reverbnation.com"
    assert customer.gender == "Female"
    assert customer.company == "Meezzy"
    assert customer.city == "Warner, NH"
    assert customer.title == "Biostatistician III"
    assert str(customer) == customer.first_name
