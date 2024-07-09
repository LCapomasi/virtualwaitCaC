from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def reservar_turno(request):
    return render(request, 'core/ReservarTurno.html')

def mis_turnos(request):
    return render(request, 'core/MisTurnos.html')

def preguntas_frecuentes(request):
    return render(request, 'core/PreguntasFrecuentes.html')