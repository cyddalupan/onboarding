from django.urls import path
from .views import JobsCreateView, JobsRetrieveUpdateDeleteView

urlpatterns = [
    path('', JobsCreateView.as_view(), name='jobs-list-create'),
    path('<int:pk>/', JobsRetrieveUpdateDeleteView.as_view(), name='jobs-detail'),
]