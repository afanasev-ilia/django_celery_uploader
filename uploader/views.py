from rest_framework import mixins, viewsets

from uploader.serializers import FileSerializer
from uploader.models import File


class FileCreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = File.objects.all()
    serializer_class = FileSerializer
