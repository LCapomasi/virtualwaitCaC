from django.shortcuts import render
from .forms import TurnoForm
from .models import Turno

# Create your views here.
def reserva_turnos (request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formulario_exito.html')
        else:
            return render(request, 'reservaturnos/reservaturnos.html', {'form': form})
    else:
        form = TurnoForm()
        return render(request, 'reservaturnos/reservaturnos.html', {'form': form})

def mis_turnos(request):
    turnos = None
    if request.method == 'POST':
        dni = request.POST.get('dni')
        turnos = Turno.objects.filter(dni=dni)
    return render(request, 'reservaturnos/MisTurnos.html', {'turnos': turnos})
