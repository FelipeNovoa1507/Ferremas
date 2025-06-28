from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciar/', views.iniciar_pago, name='iniciar_pago'),
    path('respuesta/', views.respuesta_pago, name='respuesta_pago'),
]