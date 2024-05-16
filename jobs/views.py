from rest_framework import generics
from .serializers import JobsSerializer
from .models import Job

class JobsCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer

class JobsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
