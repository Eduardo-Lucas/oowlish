import json

import pytest

from customers.models import Customer


@pytest.mark.django_db
def test_add_customer(client):
    customers = Customer.objects.all()
    assert len(customers) == 0

    resp = client.post(
        "/api/customers/",
        {
            "first_name": "Laura",
            "last_name": "Richards",
            "email": "lrichards0@reverbnation.com",
            "gender": "Female",
            "company": "Meezzy",
            "city": "Warner, NH",
            "title": "Biostatistician III",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["first_name"] == "Laura"

    customers = Customer.objects.all()
    assert len(customers) == 1
