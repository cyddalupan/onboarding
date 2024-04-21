from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CustomerSerializer
from .models import Customer

class CustomerCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            customer = get_object_or_404(Customer, username=username)
        except Customer.DoesNotExist:
            return Response({'error': 'Username incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

        if customer.password != password:
            return Response({'error': 'Password incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)