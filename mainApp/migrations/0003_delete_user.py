# Generated by Django 5.0.6 on 2024-07-29 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_buyer_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
