# Generated by Django 4.1.4 on 2022-12-25 21:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=400)),
                ('studied_in', models.CharField(max_length=400)),
                ('res_desc', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
