from django.test import TestCase, Client
from .models import Camera, Comment


# Test para el modelo Camera
class CameraEndToEndTest(TestCase):
    # Creo un cliente de prueba y un objeto camara para las pruebas
    def setUp(self):
        self.client = Client()
        self.camera = Camera.objects.create(identifier='1', name='Test Camera', image_url='http://test.com')

    # Confirmo que la pagina de la camara se carga correctamente
    def test_camera_page(self):
        response = self.client.get(f'/camera/{self.camera.identifier}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['camera'], self.camera)


class CommentEndToEndTest(TestCase):
    # Creo un cliente de prueba, una camara y un comentario para las pruebas
    def setUp(self):
        self.client = Client()
        self.camera = Camera.objects.create(identifier='1', name='Test Camera', image_url='http://test.com')
        self.comment = Comment.objects.create(camera=self.camera, text='Test comment')

    # Confirmo que la pagina de comentarios se carga correctamente
    def test_comment_page(self):
        response = self.client.get(f'/comentar/{self.camera.identifier}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['camera'], self.camera)
