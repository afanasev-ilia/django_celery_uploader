from rest_framework import serializers

from uploader.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'file',
            'uploaded_at',
            'processed',
        )
