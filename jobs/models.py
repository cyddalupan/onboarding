from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=150)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    company_email = models.EmailField()
    company_contacts = models.CharField(max_length=100)
    company_map = models.CharField(max_length=280)
    profile_image = models.ImageField(upload_to='static/images/job_profile_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=150)
    company_logo = models.ImageField(upload_to='static/images/company_logos/')

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/job_gallery/')

    def __str__(self):
        return f"Image for {self.job.title}"