
from django.contrib import admin
from django.urls import path, include
from cliente.views import modoAdmin
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagos/', include('pagos.urls')),  # Este debe estar
    path('cliente/', include('cliente.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('modoAdmin', modoAdmin, name='modoAdmin'), 
    path('', RedirectView.as_view(url='/cliente/login', permanent=False)),
]
