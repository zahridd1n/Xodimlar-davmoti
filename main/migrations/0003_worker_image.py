# Generated by Django 5.0.4 on 2024-04-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_worker_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='image',
            field=models.ImageField(null=True, upload_to='workers/'),
        ),
    ]