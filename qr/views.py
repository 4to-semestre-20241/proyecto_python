from django.shortcuts import render

import qrcode

# Create your views here.
def principal(request):
  return render(request, 'qr/principal.html', {})
  
def codificar(request):
  return render(request, 'qr/codificar.html', {})
  
def codificar_resultado(request):
  color = (0, 0, 0) # black
  qr = qr.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data('Some data')
  qr.make(fit=True)

  img = qr.make_image(fill_color=color, back_color="white")
  return render(request, 'qr/codificar_resultado.html', {})
  
def creditos(request):
  return render(request, 'qr/creditos.html', {})
  
def decodificar(request):
  return render(request, 'qr/decodificar.html', {})
