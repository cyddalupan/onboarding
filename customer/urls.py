from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomerCreateView, CustomerLoginView, CustomerRetrieveUpdateDeleteView

urlpatterns = [
    path('', CustomerCreateView.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-detail'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
]