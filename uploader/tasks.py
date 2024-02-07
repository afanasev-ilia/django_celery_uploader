from celery import shared_task

from uploader.models import File


@shared_task
def process_uploaded_file(file_id) -> None:
    file = File.objects.get(pk=file_id)
    file.processed = True
    file.save()
