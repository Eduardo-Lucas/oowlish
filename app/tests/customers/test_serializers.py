import pytest as pytest

from customers.models import Customer
from customers.serializers import CustomerSerializer


def test_valid_customer_serializer():
    valid_serializer_data = {
        "first_name": "Eduardo",
        "last_name": "Lucas",
        "email": "eduardolucas40@gmail.com",
        "gender": "Male",
        "company": "HelloGym",
        "city": "Salvador",
        "title": "Data Protection Officer",
        "latitude": 35.929673,
        "longitude": 35.929673,

    }
    serializer = CustomerSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_customer_serializer():
    invalid_serializer_data = {
        "first_name": "Eduardo",
        "last_name": "Lucas",
        "email": "eduardolucas40@gmail.com",
        "gender": "Male",
        "company": "HelloGym",
        "city": "Salvador",
    }
    serializer = CustomerSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"title": ["This field is required."]}


@pytest.mark.django_db
def test_add_customer_invalid_json(client):
    customers = Customer.objects.all()
    assert len(customers) == 0

    resp = client.post(
        "/api/customers/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    customers = Customer.objects.all()
    assert len(customers) == 0


@pytest.mark.django_db
def test_add_customer_invalid_json_keys(client):
    customers = Customer.objects.all()
    assert len(customers) == 0

    resp = client.post(
        "/api/customers/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    customers = Customer.objects.all()
    assert len(customers) == 0


@pytest.mark.django_db
def test_get_single_customer(client, add_customer):
    customer = add_customer(first_name="Laura", last_name="Richards", email="lrichards0@reverbnation.com",
                            gender="Female", company="Meezzy", city="Warner, NH",
                            title="Biostatistician III", latitude=35.929673, longitude=-78.948237,)
    resp = client.get(f"/api/customers/{customer.id}/")
    assert resp.status_code == 200
    assert resp.data["first_name"] == "Laura"


def test_get_single_customer_incorrect_id(client):
    resp = client.get(f"/api/customers/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_customers(client, add_customer):
    customer_one = add_customer(first_name="Laura", last_name="Richards", email="lrichards0@reverbnation.com",
                                gender="Female", company="Meezzy", city="Warner, NH",
                                title="Biostatistician III", latitude=35.929673, longitude=-78.948237)
    customer_two = add_customer(first_name="Margaret", last_name="Mendoza", email="mmendoza1@sina.com.cn",
                                gender="Female", company="Skipfire", city="East Natchitoches, PA",
                                title="VP Marketing", latitude=35.929673, longitude=-78.948237)
    resp = client.get(f"/api/customers/")
    assert resp.status_code == 200
    assert resp.data[0]["first_name"] == customer_one.first_name
    assert resp.data[1]["first_name"] == customer_two.first_name
