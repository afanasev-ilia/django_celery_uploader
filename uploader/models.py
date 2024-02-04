from django.db import models


class File(models.Model):
    file = models.FileField(
        'файл',
        upload_to='files/',
        help_text='добавьте файл',
    )
    uploaded_at = models.DateTimeField(
        'дата загрузки',
        auto_now_add=True,
        help_text='дата загрузки',
    )
    processed = models.BooleanField(
        'статус обработки',
        default=False,
        help_text='статус обработки',
    )
