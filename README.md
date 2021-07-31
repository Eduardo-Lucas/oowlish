![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)

# Managing Customers
## The task at hand:
- Create a simple Django REST API which provides information about customers.
- Create a django management command to import the customers.csv file into your database;  
- Create two extra fields for latitude and, longitude and, fill them up by customer's address using any 
 Geolocation API
- Implement a REST API with two endpoints: one for listing all customers and, another one for getting
a single customer by its id 
- Create a simple web page to consume the REST API (you can use auto-documentation like djangoyasg);
S. 
- Write README.md instructions on how to get your code up-and-running;

## Strategy used to import the csv file into the database
1. The database was update by installing the following package:
   ```
   pip install django-import-export
   ```
   And the file was uploaded through the Admin Panel
   

2. To update the two newly created fields latitude and longitude:
   
   pandas was used to read the csv file and update the database fields latitude and longitude

   ```
   df = pd.read_csv('customers.csv')
   ```
   A loop updated each row of the table
   ```
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
   ``` 
## How to install
- First, clone the repo
```
git clone https://github.com/Eduardo-Lucas/oowlish.git
```
- Then, fire up the container
```
docker-compose up -d
```
- Finally, navigate to [localhost:8009][1] in order to see the first page 

[1]: http://localhost:8009

## How to use

- That is the first page
![img.png](img.png)
  
- To see all the customers
![img_1.png](img_1.png)
  
- To see only one customer
![img_2.png](img_2.png)
  
## Contact
- Eduardo Lucas
- Cell phone: (55) 71 99118-2592
- E-mail: eduardolucas40@gmail.com