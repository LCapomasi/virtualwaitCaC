from django.urls import path
from . import views
from django.conf import settings 

urlpatterns = [

    # Asegúrate de agregar rutas para las otras páginas
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)