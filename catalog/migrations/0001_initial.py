# Generated by Django 4.2 on 2025-06-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('page_count', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
            ],
        ),
    ]
