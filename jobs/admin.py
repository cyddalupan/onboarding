from django.contrib import admin
from django.utils.html import mark_safe
from .models import Job, GalleryImage, JobVideo

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"

    image_tag.short_description = 'Gallery Image'
    fields = ('image', 'image_tag',)
    readonly_fields = ('image_tag',)

class JobVideoInline(admin.TabularInline):
    model = JobVideo
    extra = 3

    def video_tag(self, obj):
        if obj.video:
            return mark_safe(f'<video width="320" height="240" controls><source src="{obj.video.url}" type="video/mp4">Your browser does not support the video tag.</video>')
        return "No Video"

    video_tag.short_description = 'Video'
    fields = ('video', 'video_tag',)
    readonly_fields = ('video_tag',)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'company_name', 'referral_code', 'date_created')
    list_filter = ('company_name', 'date_created')
    search_fields = ('title', 'company_name')
    readonly_fields = ('date_created',)
    inlines = [GalleryImageInline, JobVideoInline]

admin.site.register(Job, JobAdmin)
admin.site.register(GalleryImage)
admin.site.register(JobVideo)
