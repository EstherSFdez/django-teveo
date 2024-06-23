# Generated by Django 5.0.3 on 2024-05-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_camera_source_comment_nombre"),
    ]

    operations = [
        migrations.AddField(
            model_name="camera",
            name="votes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="comment",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="camera",
            name="source",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="comment",
            name="nombre",
            field=models.CharField(default="Anónimo", max_length=255),
        ),
    ]