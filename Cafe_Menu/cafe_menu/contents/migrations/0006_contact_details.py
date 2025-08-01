# Generated by Django 5.2.1 on 2025-05-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
