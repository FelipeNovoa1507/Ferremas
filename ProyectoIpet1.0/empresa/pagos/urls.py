from django.urls import path
from .views import iniciar_pago, confirmar_pago

urlpatterns = [
    path('iniciar_pago/', iniciar_pago, name='iniciar_pago'),
    path('confirmar_pago/', confirmar_pago, name='confirmar_pago'),
    ]