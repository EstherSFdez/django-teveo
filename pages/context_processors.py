from .models import Camera, Comment


# Variables globales para todos los templates
def counts(request):
    return {
        'cameras_count': Camera.objects.count(),
        'comments_count': Comment.objects.count(),
    }


def global_context(request):
    return {
        'commenter_name': request.session.get('commenter_name', 'Anónimo'),
        'font_size': request.session.get('font_size', 'medium'),
        'font_type': request.session.get('font_type', 'Arial'),
    }

