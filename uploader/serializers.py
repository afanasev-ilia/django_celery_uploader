from rest_framework import serializers

from uploader.tasks import process_uploaded_file
from uploader.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'file',
            'uploaded_at',
            'processed',
        )
        read_only_fields = ('processed',)

    def create(self, validated_data) -> File:
        file = File.objects.create(file=validated_data['file'])
        print(type(file.id))
        print(file.id)
        process_uploaded_file.delay(file.id)
        return file
