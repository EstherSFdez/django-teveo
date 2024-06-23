import requests
from xml.etree import ElementTree as ET
from .models import Camera


# Funcion para descargar datos de las camaras
def download_camera_data():
    # URL del archivo XML
    url = 'https://gitlab.eif.urjc.es/cursosweb/2023-2024/final-teveo/-/raw/main/listado1.xml'

    # Hacer la solicitud HTTP
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear los datos XML
        root = ET.fromstring(response.content)

        # Iterar sobre los elementos 'camara' o 'cam'
        for camara in root.findall('camara') + root.findall('cam'):
            # Extraer los datos
            identifier = 'L1-' + camara.find('id').text
            name = camara.find('lugar').text if camara.find('lugar') is not None else camara.find('info').text
            image_url = camara.find('src').text if camara.find('src') is not None else camara.find('url').text

            # Crear o actualizar el objeto Camera
            Camera.objects.update_or_create(identifier=identifier, defaults={'name': name, 'image_url': image_url})


def download_camera_data_list2():
    # URL del archivo XML
    url = 'https://gitlab.eif.urjc.es/cursosweb/2023-2024/final-teveo/-/raw/main/listado2.xml'

    # Hacer la solicitud HTTP
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear los datos XML
        root = ET.fromstring(response.content)

        # Iterar sobre los elementos 'cam'
        for camara in root.findall('cam'):
            # Extraer los datos
            identifier = 'L2-' + camara.get('id')
            name = camara.find('info').text
            image_url = camara.find('url').text

            # Crear o actualizar el objeto Camera
            Camera.objects.update_or_create(identifier=identifier, defaults={'name': name, 'image_url': image_url})
