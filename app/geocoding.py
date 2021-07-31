import pandas as pd
import requests
import json

# Gonna read customers csv
from customers.models import Customer

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

    # df.at[i, 'latitude'] = lat
    # df.at[i, 'longitude'] = lng

    customer = Customer.objecs.get(id=df.at[i, 'id'])
    if customer.first_name == df.at[i, 'first_name']:
        print(df.at[i, 'id'], df.at[i, 'first_name'], apiAddress, lat, lng)


# Save data to csv with geodata
# df.to_csv('customerGeo.csv')
