# Generated by Django 5.0.1 on 2024-05-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebay_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='initial_bid',
        ),
    ]
