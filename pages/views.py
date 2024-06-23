from random import choice
from xml.etree import ElementTree as ET

import requests
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Count
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import CommentForm, ConfigForm
from .models import Camera, Comment
from .utils import download_camera_data, download_camera_data_list2
from django.db.models.functions import Substr, Cast


# Renderiza la pagina principal con su contenido
def main_page(request):
    comments_list = Comment.objects.all().annotate(
        camera_id_as_int=Cast('camera__identifier', models.IntegerField())
    ).order_by('-timestamp')
    paginator = Paginator(comments_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'cameras_count': Camera.objects.count(),
        'comments_count': Comment.objects.count(),
    }

    return render(request, 'main_page.html', context)


# Renderiza la pagina de la camara estatica con su contenido
def camera_page(request, camera_id):
    camera = get_object_or_404(Camera, identifier=camera_id)
    comments = Comment.objects.filter(camera=camera).order_by('-timestamp')
    return render(request, 'camera_page.html', {'camera': camera, 'comments': comments})


# Renderiza la pagina de la camara dinamica con su contenido
def dynamic_camera_page(request, camera_id):
    camera = get_object_or_404(Camera, identifier=camera_id)
    comments = Comment.objects.filter(camera=camera).order_by('-timestamp')
    return render(request, 'dynamic_camera_page.html', {'camera': camera, 'comments': comments})


# Renderiza la pagina de las camaras con su contenido
def cameras_page(request):
    cameras = Camera.objects.annotate(
        camera_id_as_int=Cast(Substr('identifier', 4), models.IntegerField()),
        comments_count=Count('comments')
    ).order_by('camera_id_as_int')
    for camera in cameras:
        camera.votes_count = camera.votes
    random_camera = choice(cameras) if cameras else None
    paginator = Paginator(cameras, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'random_camera': random_camera,
    }
    return render(request, 'cameras_page.html', context)


# Renderiza la pagina de comentarios con su contenido
def comment_page(request, camera_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            camera = get_object_or_404(Camera, identifier=camera_id)
            comment.camera = camera
            comment.nombre = request.session.get('commenter_name', 'Anónimo')

            # Referenciar la imagen de la cámara en lugar de descargarla
            comment.image_url = camera.image_url

            comment.save()
            return redirect('camera_page', camera_id=camera_id)
    else:
        form = CommentForm()

    camera = get_object_or_404(Camera, identifier=camera_id)
    current_time = timezone.now()

    return render(request, 'comment_page.html',
                  {'form': form, 'camera': camera, 'current_time': current_time})


# Renderiza la pagina de configuracion con su contenido
def config_page(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            # Se guarda configuracion del usuario
            request.session['commenter_name'] = form.cleaned_data['commenter_name']
            request.session['font_size'] = form.cleaned_data['font_size']
            request.session['font_type'] = form.cleaned_data['font_type']
            return HttpResponseRedirect(reverse('main_page'))
    else:
        form = ConfigForm()
    return render(request, 'config_page.html', {'form': form})


# Renderiza la pagina de ayuda con su contenido
def help_page(request):
    return render(request, 'help_page.html')


# Devuelve objeto JSON con los datos de la camara
def camera_json(request, camera_id):
    camera = get_object_or_404(Camera, identifier=camera_id)
    data = {
        'identifier': camera.identifier,
        'name': camera.name,
        'image_url': camera.image_url,
        'source': camera.source,
        'comments_count': camera.comments.count(),
    }
    return JsonResponse(data)


# Descarga los datos de las camaras y redirige a la pagina de camaras
def download_camera_data_view(request):
    download_camera_data()
    return redirect('cameras_page')


def download_camera_data_view_list2(request):
    download_camera_data_list2()
    return redirect('cameras_page')


# Cierra la sesion del usuario y redirige a la pagina principal
def logout_view(request):
    request.session.flush()
    return redirect('main_page')


# Incrementa el contador de votos de la camara y redirige a la pagina de la camara
def vote_camera(request, camera_id):
    camera = get_object_or_404(Camera, identifier=camera_id)
    camera.votes += 1
    camera.save()
    return redirect('camera_page', camera_id=camera_id)


