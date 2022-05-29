from django.urls import path
from familia.views import views
from familia.views import viewsMoto



urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
    path('moto/', viewsMoto.indexMoto, name="indexMoto"),
    path('agregarMoto/', viewsMoto.agregar, name="agregarMoto"),
    path('borrarMoto/<identificador>', viewsMoto.borrar, name="borrarMoto"),
    path('buscarMoto/', viewsMoto.buscar, name="buscarMoto"),
]
