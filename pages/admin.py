from django.contrib import admin
from .models import Camera, Comment


class CameraAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('camera', 'timestamp', 'text')
    list_filter = ('camera',)  # Filtrar comentarios por cámara


# Registro los modelos camera y comment
admin.site.register(Camera, CameraAdmin)
admin.site.register(Comment, CommentAdmin)
