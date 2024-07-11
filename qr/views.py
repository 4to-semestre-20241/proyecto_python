from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render

import qrcode

# Create your views here.
def principal(request):
  return render(request, 'qr/principal.html', {})
  
def codificar(request):
  return render(request, 'qr/codificar.html', {})
  
def codificar_resultado(request):
  colores = {
    'negro': '#000000',
    'azul': '#0369a1',
    'gris': '#374151',
    'rojo': '991b1b',
    'rosa': '#9d174d',
    'morado': '#6b21a8',
    'verde': '#166534'
  }
  tamanos = [3, 5, 10, 15, 20]

  color = (0, 0, 0) # black
  tamano = tamanos[0]
  texto = 'Hola Mundo'

  if 'texto' in request.POST and len(request.POST['texto']):
    texto = request.POST['texto']

  if 'color' in request.POST and request.POST['color'] in colores.keys():
    color = colores.get(request.POST['color'])

  if 'tamano' in request.POST and int(request.POST['tamano']) in tamanos:
    tamano = int(request.POST['tamano'])

  return render(request, 'qr/codificar__resultado.html', {
    'texto': texto,
    'tamano': tamano,
    'color': color
  })
  
def creditos(request):
  colaboradores = [
    {
      'nombre': 'Milagros Lopez',
      'nombre_usuario': 'MilaLopz',
      'link': 'https://github.com/Milalopz',

      'nombre': 'Brayan Rodriguez',
      'nombre_usuario': 'Rodricxzel',
      'link': 'https://github.com/Rodricxzel'
    }
  ]
  return render(request, 'qr/creditos.html', {'colaboradores': colaboradores})
  
def decodificar(request):
  texto = ''
  if 'img' in request.FILES:
    img = Image.open(request.FILES['img'])
    datos = decode(img)
    if datos:
      for obj in datos:
        texto += obj.data.decode('utf-8')
    else:
      texto = 'Error al procesar imagen'

  return render(request, 'qr/decodificar.html', {'resultado': texto})
