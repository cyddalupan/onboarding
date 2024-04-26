from django.contrib import admin
from django.utils.html import mark_safe
from .models import Job, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3  # Number of extra fields to show

    def image_tag(self, obj):
        # Display an image tag for the gallery image
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')

    image_tag.short_description = 'Gallery Image'  # Set the column header for the image

    fields = ('image_tag',)  # Customize fields to display in the inline form
    readonly_fields = ('image_tag',)  # Make image_tag readonly

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'company_name', 'date_created')
    list_filter = ('company_name', 'date_created')
    search_fields = ('title', 'company_name')
    readonly_fields = ('date_created',)
    inlines = [GalleryImageInline]  # Add the inline for GalleryImage

admin.site.register(Job, JobAdmin)
admin.site.register(GalleryImage)
