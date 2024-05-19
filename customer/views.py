from django.shortcuts import get_object_or_404
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Favorite
from jobs.models import Job
from .serializers import FavoriteSerializer
from .utils import send_custom_email

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

        # Login successful, generate and assign token
        customer.generate_and_assign_token()

        # Serialize customer data including the generated token
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddFavoriteView(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        job_id = request.data.get('job_id')

        customer = get_object_or_404(Customer, id=customer_id)
        job = get_object_or_404(Job, id=job_id)
        
        # Check if already favorited
        if Favorite.objects.filter(customer=customer, job=job).exists():
            return Response({'message': 'Job already added to favorites'}, status=status.HTTP_400_BAD_REQUEST)
        
        favorite = Favorite.objects.create(customer=customer, job=job)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteFavoriteView(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        job_id = request.data.get('job_id')

        customer = get_object_or_404(Customer, id=customer_id)
        job = get_object_or_404(Job, id=job_id)

        favorite = Favorite.objects.filter(customer=customer, job=job).first()
        
        if not favorite:
            return Response({'message': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
        
        favorite.delete()
        return Response({'message': 'Favorite removed'}, status=status.HTTP_204_NO_CONTENT)
class ListFavoritesView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')  # Fetch the customer_id from URL parameters
        customer = get_object_or_404(Customer, id=customer_id)
        return Favorite.objects.filter(customer=customer)

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            customer = get_object_or_404(Customer, email=email)
        except Customer.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Send the current password via email
        subject = "Your Password Information"
        message = f"""Dear {customer.firstname},

            We are reaching out to provide you with your current password. Please find it below:

            **Password:** {customer.password}

            At Dirrect Application, we are committed to empowering Filipinos to reach new horizons.
            If you have any questions or need further assistance, please don't hesitate to contact our support team.

            Best regards,

            The Dirrect Application Team

            Empowering Filipinos to Reach New Horizons
            """
        send_custom_email(subject, message, [email])
        
        return Response({'message': 'Password has been sent to your email'}, status=status.HTTP_200_OK)