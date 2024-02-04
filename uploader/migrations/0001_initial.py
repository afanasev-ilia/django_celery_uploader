# Generated by Django 3.2 on 2024-02-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='добавьте файл', upload_to='files/', verbose_name='файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, help_text='дата загрузки', verbose_name='дата загрузки')),
                ('processed', models.BooleanField(default=False, help_text='статус обработки', verbose_name='статус обработки')),
            ],
        ),
    ]