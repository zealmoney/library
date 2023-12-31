# Generated by Django 4.2 on 2023-04-17 17:47

from django.db import migrations, models
import library_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('about', models.TextField()),
                ('author_image', models.ImageField(upload_to=library_app.models.author_upload_to)),
            ],
        ),
    ]
