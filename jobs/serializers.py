from rest_framework import serializers
from .models import Job

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'salary', 'description', 'company_email', 'company_contacts', 'company_map', 'profile_image', 'company_name', 'company_logo', 'date_created']
        read_only_fields = ['id', 'date_created']
