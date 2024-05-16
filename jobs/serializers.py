from rest_framework import serializers
from .models import Job, GalleryImage, JobVideo

class JobVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobVideo
        fields = ['id', 'video']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class JobsSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True, read_only=True)
    job_videos = JobVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'salary', 'description', 'company_email', 'company_contacts', 
            'company_map', 'profile_image', 'company_name', 'company_logo', 'date_created',
            'gallery_images', 'job_videos'
        ]
        read_only_fields = ['id', 'date_created']
