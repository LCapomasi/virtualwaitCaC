from django.urls import path
from . import views
from django.conf import settings 

urlpatterns = [
    path('', views.home, name='home'),
    # Asegúrate de agregar rutas para las otras páginas
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('reservar-turno/', views.reservar_turno, name='reservar_turno'),
    path('mis-turnos/', views.mis_turnos, name='mis_turnos'),
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)