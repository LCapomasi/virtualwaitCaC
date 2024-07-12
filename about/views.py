from django.shortcuts import render
from .models import Project

# Create your views here.

def sobre_nosotros(request):
    projects = Project.objects.all()
    return render(request, 'about/SobreNosotros.html', {'projects':projects})