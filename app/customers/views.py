from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import Geolocation
from .models import Customer
from .serializers import CustomerSerializer

import pandas as pd
import requests
import json


class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


def update_geolocation(request):
    customers = []
    form = Geolocation()
    if request.method == 'POST':
        df = pd.read_csv('customers.csv')

        # API call and get the latitude and longitude values
        for i, row in df.iterrows():
            apiAddress = df.at[i, 'city']

            parameters = {
                'key': 'widkeGelUHsZShDH5wsUTaTqySc59Va0',
                'location': apiAddress
            }
            response = requests.get('http://www.mapquestapi.com/geocoding/v1/address',
                                    params=parameters)
            data = json.loads(response.text)['results']

            lat = data[0]['locations'][0]['latLng']['lat']
            lng = data[0]['locations'][0]['latLng']['lng']

            customer = Customer.objects.get(id=df.at[i, 'id'])
            customer.latitude = lat
            customer.longitude = lng

            # Save data to the database with geolocation
            customer.save()

            customers.append(customer)

    context = {
        'customers': customers,
        'form': form,
    }
    return render(request, 'customers/update_geolocation.html', context)
