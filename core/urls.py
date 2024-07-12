
<<<<<<< HEAD
=======
urlpatterns = [
    path('', views.home, name='home'),
    # Asegúrate de agregar rutas para las otras páginas
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
>>>>>>> 81698c865784b87c2e1811058eec02ec610a2472