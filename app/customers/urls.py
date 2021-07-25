from django.urls import path

from .views import CustomerList, CustomerDetail

urlpatterns = [
    path("api/customers/", CustomerList.as_view()),
    path("api/customers/<int:pk>/", CustomerDetail.as_view()),
]
