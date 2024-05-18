from django.urls import path
from .views import (
    CustomerCreateView, CustomerLoginView, CustomerRetrieveUpdateDeleteView,
    AddFavoriteView, ListFavoritesView, DeleteFavoriteView
)

urlpatterns = [
    path('', CustomerCreateView.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-detail'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
    path('favorites/<int:customer_id>/', ListFavoritesView.as_view(), name='favorites-list'),
    path('favorites/add/', AddFavoriteView.as_view(), name='add-favorite'),
    path('favorites/delete/', DeleteFavoriteView.as_view(), name='delete-favorite'),  # New URL pattern
]
