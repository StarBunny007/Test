# Generated by Django 5.0.6 on 2024-07-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assigned',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
