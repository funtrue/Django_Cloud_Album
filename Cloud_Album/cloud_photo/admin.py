from django.contrib import admin
from cloud_photo.models import Photo
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = "云相册管理端"

class PhotoAdmin(ImportExportModelAdmin):
    list_display = ('image', 'created_time')

admin.site.register(Photo,PhotoAdmin)