from django.urls import path
from . import views
from django.conf import settings 

urlpatterns = [

    # Asegúrate de agregar rutas para las otras páginas
    path('reserva-turnos/', views.reserva_turnos, name='reserva_turnos'),
    path('mis-turnos/', views.mis_turnos, name='mis_turnos'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
