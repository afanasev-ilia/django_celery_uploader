from django.urls import path

from uploader.views import FileCreateListViewSet


urlpatterns = [
    path(
        'files/',
        FileCreateListViewSet.as_view({'get': 'list'}),
        name='files',
    ),
    path(
        'upload/',
        FileCreateListViewSet.as_view({'post': 'create'}),
        name='upload',
    ),
]
