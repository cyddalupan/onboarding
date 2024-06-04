from django.db import models
from jobs.models import Job
import random
import string

# Create your models here.

def generate_random_token():
    token_length = 50  # Set the desired length of the token
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(token_length))

class Customer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    token = models.CharField(max_length=100, blank=True)
    is_activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_forgot_password = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def generate_and_assign_token(self):
        self.token = generate_random_token()
        self.save()

class Attachment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    file = models.FileField(upload_to='static/customer_attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.customer.firstname} {self.customer.lastname}"

class Favorite(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'job')

    def __str__(self):
        return f"{self.customer.username} favorited {self.job.title}"