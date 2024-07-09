from django.shortcuts import render

# Create your views here.

def sobre_nosotros(request):
    return render(request, 'about/SobreNosotros.html')
