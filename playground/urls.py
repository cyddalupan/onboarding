from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ActionsGPTWebhook

router = DefaultRouter()

urlpatterns = [
    path('actions-gpt-webhook/', ActionsGPTWebhook.as_view(), name='actions-gpt-webhook'),
]

