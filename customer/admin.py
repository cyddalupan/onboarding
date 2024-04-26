from django.contrib import admin
from django.utils.html import mark_safe
from .models import Customer, Attachment

class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 3  # Number of extra fields to show

    def get_queryset(self, request):
        # Override queryset to prefetch the related file URLs for each attachment
        qs = super().get_queryset(request)
        return qs.select_related('customer')

    def image_tag(self, obj):
        # Display an image tag for the file if it's an image type
        if obj.file.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return mark_safe(f'<img src="{obj.file.url}" width="100" height="100" />')
        return None

    image_tag.short_description = 'Attachment Image'  # Set the column header for the image

    fields = ('image_tag', 'file', 'uploaded_at')  # Customize fields to display in the inline form
    readonly_fields = ('image_tag', 'uploaded_at')  # Make image_tag and uploaded_at readonly

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', 'mobile', 'created_at')
    search_fields = ('username', 'firstname', 'lastname', 'email')
    readonly_fields = ('created_at',)
    inlines = [AttachmentInline]  # Add the inline for Attachment

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Attachment)
