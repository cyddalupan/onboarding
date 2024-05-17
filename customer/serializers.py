from rest_framework import serializers
from jobs.serializers import JobsSerializer
from .models import Customer, Favorite

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'firstname', 'lastname', 'email', 'mobile', 'token', 'created_at']
        read_only_fields = ['id', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    job = JobsSerializer(read_only=True)
    
    class Meta:
        model = Favorite
        fields = ['id', 'job', 'added_on']
        read_only_fields = ['id', 'added_on']