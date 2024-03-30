from django.contrib import admin
from .models import Job, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3  # Number of extra fields to show

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'company_name', 'date_created')
    list_filter = ('company_name', 'date_created')
    search_fields = ('title', 'company_name')
    readonly_fields = ('date_created',)

admin.site.register(Job, JobAdmin)
admin.site.register(GalleryImage)