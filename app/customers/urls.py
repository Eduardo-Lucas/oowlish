from django.urls import path

from .views import CustomerList, CustomerDetail, update_geolocation

urlpatterns = [
    path("api/customers/", CustomerList.as_view()),
    path("api/customers/<int:pk>/", CustomerDetail.as_view()),
    path("update_geolocation/", update_geolocation,
         name='update_geolocation'),
]
