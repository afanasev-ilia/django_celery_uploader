from django.contrib import admin

from uploader.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
        'uploaded_at',
        'processed',
    )
    empty_value_display = '-пусто-'
