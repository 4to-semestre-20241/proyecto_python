from django.shortcuts import render

# Create your views here.
def principal(request):
  return render(request, 'qr/principal.html')
  
def codificar(request):
  return render(request, 'qr/codificar.html')
  
def codificar_resultado(request):
  return render(request, 'qr/codificar_resultado.html')
  
def creditos(request):
  return render(request, 'qr/creditos.html')
  
def decodificar(request):
  return render(request, 'qr/decodificar.html')
