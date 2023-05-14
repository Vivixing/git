"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
#from django.urls import include
from  app_restaurante.views import ComidaListado, Index, ComidaDetalle,ComidaCrear,ComidaActualizar,ComidaEliminar, UsuarioActualizar, UsuarioCrear, UsuarioDetalle, UsuarioEliminar, UsuarioListado, PedidoActualizar, PedidoCrear, PedidoDetalle, PedidoEliminar, PedidoListado, VistaPrincipalView
#from .views import principal
#from .views import principal
#from app_restaurante.views import principal
from django.views.generic import RedirectView
from django.views.static import serve




urlpatterns = [
    #urls para la vista del usuario
   path('vista_usuario/vistaPrincipal', VistaPrincipalView.as_view(), name='vista_principal'),
   path('vista_usuario/vistaVegetariana', VistaPrincipalView.as_view(template_name="vista_usuario/vistaVegetariana.html"), name='vistaVegetariana'),
   path('vista_usuario/vistaVegano', VistaPrincipalView.as_view(template_name="vista_usuario/vistaVegano.html"), name='vistaVegano'),
   path('vista_usuario/vistaDiab', VistaPrincipalView.as_view(template_name="vista_usuario/vistaDiab.html"), name='vistaDiab'),
   path('vista_usuario/vistaBebidas', VistaPrincipalView.as_view(template_name="vista_usuario/vistaBebidas.html"), name='vistaBebidas'),
   path('vista_usuario/vistaPostre', VistaPrincipalView.as_view(template_name="vista_usuario/vistaPostre.html"), name='vistaPostre'),
   path('vista_usuario/carritoCompra', VistaPrincipalView.as_view(template_name="vista_usuario/carritoCompra.html"), name='carritoCompra'),
   path('vista_usuario/',  RedirectView.as_view(url='vistaPrincipal', permanent=False)),
   
    #urls para la vista del administrador 
    path('', RedirectView.as_view(url='principal/', permanent=False)),
 
    path('admin/', admin.site.urls),
    
    path('principal/', Index.as_view(template_name = "index.html"), name='principal'),
    
    # La ruta 'leer' en donde listamos todos los registros o arepas de la Base de Datos
    path('comida/', ComidaListado.as_view(template_name = "comida/comida.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un arepas o registro 
    path('comida/detalle/<int:pk>', ComidaDetalle.as_view(template_name = "comida/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo arepas o registro  
    path('comida/crear', ComidaCrear.as_view(template_name = "comida/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un arepas o registro de la Base de Datos 
    path('comida/actualizar/<int:pk>', ComidaActualizar.as_view(template_name = "comida/actualizar.html"), name='actualizar'), 

    # La ruta 'eliminar' que usaremos para eliminar un arepas o registro de la Base de Datos 
    
    path('comida/eliminar/<int:pk>', ComidaEliminar.as_view(template_name= "comida/eliminar.html"), name='eliminar'),

    path('usuario/', UsuarioListado.as_view(template_name = "usuario/usuario.html"), name='leer_usuario'),

    path('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "usuario/detalles.html"), name='detallesUsuario'),

    path('usuario/crear', UsuarioCrear.as_view(template_name = "usuario/crear.html"), name='crearUsuario'),

    path('usuario/actualizar/<int:pk>', UsuarioActualizar.as_view(template_name = "usuario/actualizar.html"), name='actualizarUsuario'),

    path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(template_name= "usuario/eliminar.html"), name='eliminarUsuario'),

    path('pedido/', PedidoListado.as_view(template_name = "pedido/pedido.html"), name='leer_pedido'),

    path('pedido/detalle/<int:pk>', PedidoDetalle.as_view(template_name = "pedido/detalles.html"), name='detallesPedido'),

    path('pedido/crear', PedidoCrear.as_view(template_name = "pedido/crear.html"), name='crearPedido'),

    path('pedido/actualizar/<int:pk>', PedidoActualizar.as_view(template_name = "pedido/actualizar.html"), name='actualizarPedido'),

    path('pedido/eliminar/<int:pk>', PedidoEliminar.as_view(template_name= "pedido/eliminar.html"), name='eliminarPedido'),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT,
    })
    
]
