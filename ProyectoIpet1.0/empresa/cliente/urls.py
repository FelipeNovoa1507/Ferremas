from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('logout/', views.exit, name='logout'),
    path('login', views.inicioSesion, name='cliente_login'),
    path('index', views.index, name='index'),    
    #path('modoAdmin', views.modoAdmin, name='modoAdmin'), 
    path('carrito', views.carrito, name='carrito'), 
    path('restablecercon', views.restablecercon, name='restablecercon'),
    path('registro', views.registro, name='registro'),
    path('producto_detalle/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),    
    path('listaDeseos', views.listadeseos, name='listadeseos'),
    path('listarProducto', views.listarProducto, name='listarProducto'),
    path('registroProducto', views.registroProducto, name='registroProducto'),
    path('guardarProducto', views.guardarProducto, name='guardarProducto'),
    path('gestionarProducto/<int:pk>/<str:accion>/', views.gestionarProducto, name='gestionarProducto'),
    path('listarUsuario', views.listarUsuario, name='listarUsuario'),
    path('registroUsuario', views.registroUsuario, name='registroUsuario'),
    path('guardarUsuario', views.guardarUsuario, name='guardarUsuario'),
    path('gestionarUsuario/<int:pk>/<str:accion>/', views.gestionarUsuario, name='gestionarUsuario'),
    path('gestionarListaDeseos/<str:accion>/<int:producto_id>/<str:redirigir>/', views.gestionarListaDeseos, name='gestionarListaDeseos'),
    path('gestionarListaDeseos/<str:accion>/<int:producto_id>/', views.gestionarListaDeseos, name='gestionarListaDeseos'),
    path('gestionarListaDeseos/<str:accion>/', views.gestionarListaDeseos, name='gestionarListaDeseos'),
    path('gestionarCarrito/<str:accion>/<int:producto_id>/<str:redirigir>/', views.gestionarCarrito, name='gestionarCarrito'),
    path('gestionarCarrito/<str:accion>/<int:producto_id>/', views.gestionarCarrito, name='gestionarCarrito'),
    path('gestionarCarrito/<str:accion>/', views.gestionarCarrito, name='gestionarCarrito'),
    path('listarCategoria', views.listarCategoria, name='listarCategoria'),
    path('registroCategoria', views.registroCategoria, name='registroCategoria'),
    path('guardarCategoria', views.guardarCategoria, name='guardarCategoria'),
    path('gestionarCategoria/<int:pk>/<str:accion>/', views.gestionarCategoria, name='gestionarCategoria'),
    path('listarMarca', views.listarMarca, name='listarMarca'),
    path('registroMarca', views.registroMarca, name='registroMarca'),
    path('guardarMarca', views.guardarMarca, name='guardarMarca'),
    path('gestionarMarca/<int:pk>/<str:accion>/', views.gestionarMarca, name='gestionarMarca'),
    path('listarFormaDePago', views.listarFormaDePago, name='listarFormaDePago'),
    path('registroFormaDePago', views.registroFormaDePago, name='registroFormaDePago'),
    path('guardarFormaDePago', views.guardarFormaDePago, name='guardarFormaDePago'),
    path('gestionarFormaDePago/<int:pk>/<str:accion>/', views.gestionarFormaDePago, name='gestionarFormaDePago'),
            ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
