from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Attachment

admin.site.register(Customer)
admin.site.register(Attachment)