from django.shortcuts import render
from .models import Project

# Create your views here.

def reserva_turnos(request):
    projects = Project.objects.all()
    return render(request, 'about/ReservarTurnos.html', {'projects':projects})

