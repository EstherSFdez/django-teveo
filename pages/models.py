from django.db import models


class Camera(models.Model):
    objects = None
    identifier = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    source = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    objects = None
    nombre = models.CharField(max_length=255, default='Anónimo')
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image_url = models.URLField(blank=True, null=True)  # Referencia a la URL de la imagen de la cámara

    def __str__(self):
        return f'{self.camera.name} - {self.timestamp}'
