# Generated by Django 3.2.23 on 2024-05-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebay_app', '0003_customuser_user_highest_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='displayedPrice',
            field=models.IntegerField(default=0),
        ),
    ]
