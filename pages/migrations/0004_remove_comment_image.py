# Generated by Django 5.0.3 on 2024-06-23 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_camera_votes_comment_image_url_alter_camera_source_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="image",
        ),
    ]