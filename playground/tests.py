from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class ActionsGPTWebhookTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('actions-gpt-webhook')

    def test_post_with_user_input(self):
        data = {'user_input': 'Test message'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"responses": [{"message": "Echo: Test message"}]})

    def test_post_without_user_input(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"responses": [{"message": "Echo: Hello"}]})

