from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path("camera/<str:camera_id>/", views.camera_page, name='camera_page'),
    path("camera/<str:camera_id>/json/", views.camera_json, name='camera_json'),
    path("comentar/<str:camera_id>/", views.comment_page, name='comment_page'),
    path("configuracion/", views.config_page, name='config_page'),
    path("ayuda/", views.help_page, name='help_page'),
    path("camera/<str:camera_id>/dinamica/", views.dynamic_camera_page, name='dynamic_camera_page'),
    path("cameras/", views.cameras_page, name='cameras_page'),
    path("descargar_datos/", views.download_camera_data_view, name='download_camera_data'),
    path("descargar_datos/listado2/", views.download_camera_data_view_list2, name='download_camera_data_list2'),
    path("logout/", views.logout_view, name='logout'),
    path("camera/<str:camera_id>/vote/", views.vote_camera, name='vote_camera'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
